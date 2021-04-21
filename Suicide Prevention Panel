let Discord;
let Database;
if (typeof window !== "undefined") {
    Discord = DiscordJS;
    Database = EasyDatabase;
} else {
    Discord = require("discord.js");
    Database = require("easy-json-database");
}
const delay = (ms) => new Promise((resolve) => setTimeout(() => resolve(), ms));
const s4d = {
    Discord,
    client: null,
    tokenInvalid: false,
    reply: null,
    joiningMember: null,
    database: new Database("./db.json"),
    checkMessageExists() {
        if (!s4d.client) throw new Error('You cannot perform message operations without a Discord.js client')
        if (!s4d.client.readyTimestamp) throw new Error('You cannot perform message operations while the bot is not connected to the Discord API')
    }
};
s4d.client = new s4d.Discord.Client({
    fetchAllMembers: true
});
s4d.client.on('raw', async (packet) => {
    if (['MESSAGE_REACTION_ADD', 'MESSAGE_REACTION_REMOVE'].includes(packet.t)) {
        const guild = s4d.client.guilds.cache.get(packet.d.guild_id);
        if (!guild) return;
        const member = guild.members.cache.get(packet.d.user_id) || guild.members.fetch(d.user_id).catch(() => {});
        if (!member) return;
        const channel = s4d.client.channels.cache.get(packet.d.channel_id);
        if (!channel) return;
        const message = channel.messages.cache.get(packet.d.message_id) || await channel.messages.fetch(packet.d.message_id).catch(() => {});
        if (!message) return;
        s4d.client.emit(packet.t, guild, channel, message, member, packet.d.emoji.name);
    }
});
s4d.client.on('ready', async () => {
    s4d.client.user.setActivity(String((s4d.client.ws.ping)));

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'hc!tsetup') {
        (s4d.client.guilds.cache.find((guild) => guild.name === ((s4dmessage.guild).name))).channels.create('threat-logging', {
            type: 'text'
        });
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send(String('Make sure to lock this channel to moderators only!'));
    }

});

s4d.client.on('message', async (s4dmessage) => {
    if ((s4dmessage.content) == 'suicide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill myself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 's uicide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'su icide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'sui cide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'suic ide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'suici de') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'suicid e') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'k ill yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'ki ll yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kil l yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill  yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill  yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill   yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill    yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kill urself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kil urself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kil yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'kil yourself') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Severe Warning',
                color: '#ff0000',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'go die') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'go d1e') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'commit d1e') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'su1cide') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'suic1de') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'su1c1de') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'hope you die') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'hope you d1e') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die faggot') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die fag') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e faggot') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e fag') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die kike') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e kike') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die jew') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e jew') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die nigger') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die nigga') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e nigger') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e nigga') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die n1gger') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e n1gger') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die n1gga') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e n1gga') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'just die') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'just d1e') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'die tranny') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'd1e tranny') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }
    if ((s4dmessage.content) == 'commit die') {
        s4d.client.channels.cache.find((channel) => channel.name === 'threat-logging').send({
            embed: {
                title: 'Mild Warning',
                color: '#ff6600',
                image: {
                    url: null
                },
                description: (s4dmessage.content)
            }
        });
    }

});

s4d.client.login('TOKEN').catch((e) => {
    s4d.tokenInvalid = true;
    s4d.tokenError = e;
});

s4d;
