import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os, typing, shutil
from os import system
import datetime

# Music Commands
class Music(commands.Cog):
    
    # Runs when initializing the document in the cogs
    def __init__(self, client):
        
        # Defines the client within self
        self.client = client
        # Defines the queue system within self at start
        self.queues = {}

    # Join command
    @commands.command(name='join', aliases=['jo', 'joi'], description= 'Makes the bot join the call')
    async def join(self, ctx):
        # Assigns channel and voice to variables
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # Checks if voice is already connected
        if voice is not None:
            # Moves bot to new channel if already connected to one
            return await voice.move_to(channel)
        
        # Tries to connect to call
        try:
            # Connects to channel
            await channel.connect()
            print(f"The bot has connected to {channel}\n")
            await ctx.send(f"Joined {channel}")
        
        # Alerts user if bot could not join
        except:
            print('"Join" ERROR: could not connect to channel')
            await ctx.send('Please join a message channel before playing music!')

    # Leave command
    @commands.command(name='leave', description='Makes the bot leave the call')
    async def leave(self, ctx):
        # Assigns the channel and voice connections to variables
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # checks if voice is connected to channel
        if voice and voice.is_connected():
            # disconnects voice
            await voice.disconnect()
            print(f"The bot has left {channel}!")
            await ctx.send(f"Left {channel}")
        # Alerts user if bot isn't connected to channel
        else:
            print("Bot was told to leave voice channel, but was not in one")
            await ctx.send("Don't think I am in a voice channel?")

    # Pause command
    @commands.command(name='pause', aliases=['pa', 'pau'], description= 'Pauses current playing audio')
    async def pause(self, ctx):
        # Assigns voice to a variable
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # Checks if voice is connected and playing audio
        if voice and voice.is_playing():
            # Try to pause audio
            try:
                # Pauses current audio
                voice.pause()
                print("Music paused \n")
                return await ctx.send("Music paused")
            # checks if pausing audio is unsuccessful
            except:
                # Fallback plan: clear queue and stop current audio
                try:
                    self.queues.clear()
                    voice.stop()
                    print('FALLBACK: Purged queue list due to "pause" command failure \n')
                    return await ctx.send("ERROR: Music failed to pause, purged all audio listings")
                
                # If fallback fails disconnect from call to end and clear all audio
                except:
                    voice.disconnect()
                    print('FATAL ERROR: Could not take action from the "pause command \n')
                    return await ctx.send('An error has occured, please send the *Join* or *Play* commands to allow me to rejoin the channel')
        
        # Alerts user if audio isn't playing
        else:
            print("Music not playing failed pause \n")
            await ctx.send("Music not playing failed pause")

    # Resume command # Needs enhanced error handler
    @commands.command(name= 'resume', aliases=['resum', 'res'], description= 'Resumes current paused audio')
    async def resume(self, ctx):
        # Assigns voice to a variable
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # Checks if voice is connected and if voice is paused
        if voice and voice.is_paused():
            # Resumes audio
            voice.resume()
            print("Resumed music")
            await ctx.send("Resumed music")
        
        # Alerts user no audio is paused
        else:
            print("Resume FAILED: Music is not paused")
            await ctx.send("Music is not paused")

    # Stop command
    @commands.command(name= 'stop', aliases=['st', 'sto'], description= 'Stops all of the music and ends the queue')
    async def stop(self, ctx):
        # Assigns voice to a variable
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # Clears the current queue
        self.queues.clear()

        # checks if "./Queue" is in current directory and assigns to variable
        queue_infile = os.path.isdir("./Queue")
        # If queue_infile exists remove the folder
        if queue_infile is True:
            shutil.rmtree("./Queue")

        # if voice is connected and playing audio, stop audio
        if voice and voice.is_playing():
            voice.stop()
            await voice.disconnect()
            print("Music stopped")
            await ctx.send("Music stopped")
        
        # Alerts user if command is ran but no audio is playing
        else:
            print("No music playing failed to stop")
            await ctx.send("No music playing failed to stop")

    # Next command
    @commands.command(name= 'next', aliases=['n', 'nex', 'skip', 'sk'], description= 'Skips the current playing audio')
    async def next(self, ctx):
        # assigns voice to a variable
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # checks if voice is connected and playing audio
        if voice and voice.is_playing():
            # Stops the current audio (Continues to next in queue if any items remaining)
            voice.stop()
            print(" Song Skipped: Playing next song")
            await ctx.send("Next Song")
        
        # If no audio is playing or not in a channel alert user no audio is playing
        else:
            print(" FAILED: No music playing")
            return await ctx.send("FAILED: No music playing")

    # Volume command
    @commands.command(name= 'volume', aliases=['', 'vol'], description= 'Adjusts the volume of the audio output')
    async def volume(self, ctx, volume:typing.Optional[int]=0.07):
        # Assigns voice as a variable
        voice = get(self.client.voice_clients, guild=ctx.guild)

        # Checks if voice is not connected to a voice chat
        if voice.client is None:
            return await ctx.send('Not connected to voice channel')

        # Checks if argument volume is ran as default volume 0.07 (7%)
        if volume == 7 or volume == 0.07:
            try:
                print('Volume changed to 0.07 (7%) : DEFAULT_VOLUME')
                await ctx.send('Set volume to default volume (7%)')
                # Sets volume of the client playing music
                ctx.voice_client.source.volume = 0.07
            except AttributeError:
                volume = 0.07
                
        
        # If *arg volume parsed is anything other than default volume level
        else:
            # Takes the input and converts it to a decimal
            # Client volume limits out at 5.0
            pendingVolume = volume / 100
            
            # Checks if volume > or = 100%
            if pendingVolume >= 1.0:
                # Passes volume at fixed "Max" volume 1.0 (100%)
                approvedVolume = 1.0
                ctx.voice_client.source.volume = approvedVolume
                print('Volume changed to 1.00 (100%) : MAX_VOLUME')
                await ctx.send(f'Changed volume to 100%')
            
            # Check if volume is > 0 and if volume is less than 100%
            elif pendingVolume >= 0.01 and pendingVolume < 1.0 and pendingVolume != 0.07:
                # Approves the volume
                approvedVolume = pendingVolume
                
                # Manipulates int to str and converts the output to a percentage
                if str(pendingVolume).startswith('0.') and not str(pendingVolume).startswith('0.0') and not str(pendingVolume).startswith('1.0'):
                    # Checks if volume is not count of .1
                    if len(str(pendingVolume)) > 3:
                        # removes "0." from the number (i.e. 22/100 == 0.22 strip(0.) == 22)
                        percentVolume = str(pendingVolume).replace('0.', '')
                        ctx.voice_client.source.volume = approvedVolume
                        print(f'Volume changed to {approvedVolume} ({percentVolume}%)')
                        await ctx.send(f'Changed volume to {percentVolume}%')
                    # checks if volume is count of .1
                    elif len(str(pendingVolume)) <= 3:
                        pendingVolume = str(pendingVolume).replace('0.', '')
                        percentVolume = str(pendingVolume).replace(pendingVolume, f'{pendingVolume}0')
                        ctx.voice_client.source.volume = approvedVolume
                        print(f'Volume changed to {approvedVolume} ({percentVolume}%)')
                        await ctx.send(f'Changed volume to {percentVolume}%')
                
                # passes all accepted volumes < 0.1 and > 0.0
                else:
                    if pendingVolume != 0.07:
                        percentVolume = str(pendingVolume).replace('0.0', '')
                        ctx.voice_client.source.volume = approvedVolume
                        print(f'Volume changed to {approvedVolume} ({percentVolume}%)')
                        await ctx.send(f'Changed volume to {percentVolume}%')
            
            # Checks if volume < or = 0
            else:
                if volume != 0.07 and volume <= 0:
                    # Sets all volumes < or = 0 to 0.0 (0% : Muted)
                    approvedVolume = 0.0
                    ctx.voice_client.source.volume = approvedVolume
                    print(f'Volume changed to 0.00 (0%) : MUTED')
                    await ctx.send(f'Muted the current audio')

    # Queue command
    @commands.command(name= 'play', aliases=['q', 'que', 'queue', 'queueue', 'queu', 'p', 'pl', 'pla', 'Play'], description='Adds items to a queue')
    async def queue(self, ctx, *url: str):
        
        await ctx.send('Getting everything ready for you now')
        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more queued audio\n")
                    self.queues.clear()
                    return
                main_location = os.path.dirname(os.path.abspath(os.path.realpath("Bots")))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    voice = get(self.client.voice_clients, guild=ctx.guild)
                    if voice and not voice.is_playing():
                        lineOutput = ['Song done, playing next queued', f' Songs still in queue: {still_q}']
                        for line in lineOutput:
                            print(line)
                        print(' ===============================================', ' ===============================================')
                    else:
                        print(f" Songs in queue: {still_q}")
                    
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        try:
                            os.remove("song.mp3")
                        except PermissionError:
                            return print(f' Song is currently playing, adding new song to queue position: {q_num - 1} \n',
                                         f'Current Queue Count (including current playing): {q_num}',
                                         f'\n ===============================================',
                                         f'\n ===============================================\n')
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, 'song.mp3')
                            
                    voice = get(self.client.voice_clients, guild=ctx.guild)
                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.07
 
                else:
                    self.queues.clear()
                    return
 
            else:
                self.queues.clear()
                print(" No songs were queued before the ending of the last song \n",
                      f' =============================================== \n',
                      f' =============================================== \n',)

        # Checks if Queue folder exists in same folder as running directory
        Queue_infile = os.path.isdir("./Queue")
        # If queue doesnt exist
        if Queue_infile is False:
            # Make directory for Queue
            os.mkdir("Queue")
        # Assigns new directory of queue to a variable
        DIR = os.path.abspath(os.path.realpath("Queue"))
        # Q_Num is the number of songs in the Queue folder
        global q_num
        q_num = len(os.listdir(DIR))
        # Add one to include current playing song
        q_num += 1
        
        # Checks if number exists in queue system
        add_queue = True
        while add_queue:
            # If number already exists add 1 to q_num and try again
            if q_num in self.queues:
                q_num += 1
            #if q_num is not already in the queue, add it to queue (appends to the end of the count)
            else:
                add_queue = False
                self.queues[q_num] = q_num

        # Assigns path to the audio to a variable
        queue_path = os.path.abspath(os.path.realpath("Queue") + f"\\song{q_num}.%(ext)s")

        # Sets options for youtube-dl library to use for download
        ydl_opts = {
            # Audio quality format
            'format': 'bestaudio/best',
            # Silences ydl output
            'quiet': True,
            # Sets ydl output
            'outtmpl': queue_path,
            # Additional settings 
            # (Don't touch unless you know what you are doing)
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                # File Extension
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        # Takes all arguments in url and joins them with a SPACE (" ")
        song_search = " ".join(url)
        
        # Tries to download link through Youtube Search
        # Also compatible with word searches
        dT = datetime.datetime.now()
        request_time = str(dT.strftime('%I_%M_%S %p ').replace('_', ':'))
        print(f' =============================================== \n',
              f'=============================================== \n',
              f'Request by: {ctx.message.author} \n',
              f'Song request: {song_search} \n',
              f'Time requested at: {request_time} \n',
              f'Server requested in: {ctx.guild} \n',
              f'Channel requested in: {ctx.message.channel} \n',
              f'=============================================== \n',
              f'=============================================== \n',
              f'Attempting to download audio')
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print(" Downloading audio now")
                try:
                    ydl.download([f'ytsearch1:{song_search}'])
                finally:
                    print(" Audio done downloading \n Song added to queue")
                    return await ctx.send("Adding song " + str(q_num) + " to the queue")
        
        # Triggers if youtube search failed
        except:
            print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if Spotify URL) \n")
            
            # Try to download using spotdl within system
            try:
                q_path = os.path.abspath(os.path.realpath("Queue"))
                print(" Downloading audio now")
                system(f"spotdl -ff song{q_num} -f " + '"' + q_path + '"' + " -s " + song_search)
                print("Audio done downloading \n Song added to queue")
                return await ctx.send("Adding song " + str(q_num) + " to the queue")
            
            # If song can't be downloaded, error out
            except:
                print(f"Song Search FAILED: Could not find {song_search}")
                return await ctx.send(f'I am sorry, but I could not find the song given. \n \nSong given: \n```{song_search}```')
        finally:
            check_queue()

# Sets up script to be ran as cog
def setup(client):
    client.add_cog(Music(client)) # client.add_cog({ClassName}(client))
