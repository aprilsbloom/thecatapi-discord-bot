require('dotenv').config();
const Discord = require('discord.js');
const axios = require('axios');
const { MessageEmbed } = require('discord.js');



const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] })


const Errorhandler = require("discord-error-handler");
const handle = new Errorhandler(client, {
    webhook: { id: `webhook-id`, token: `webhook-token` } 
})

process.on('unhandledRejection', error => {
    handle.createrr(client, undefined, undefined, error) // sends errors to a discord webhook and handles the errors, instead of putting the bot offline when it encounters an error
});

client.on('ready', () => {
    client.user.setActivity(`*help in ${client.guilds.cache.size} Servers `, { type: "LISTENING" })
    console.log(`Logged in as ${client.user.tag}!`);
    console.log();
    console.log('Logs:');
});



const apikeys = ["put-api-key-here", "put-api-key-here"];

const random = Math.floor(Math.random() * apikeys.length);

client.on('messageCreate', async msg => {
    switch (msg.content) {
        case "*gif":
            const gif = await getGif(); //fetches a URL from the API
            const gifembed = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat gif:')
                .setURL(gif)
                .setImage(gif)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [gifembed] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *gif in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*image":
            const img = await getImage();
            const imgembed = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat image:')
                .setURL(img)
                .setImage(img)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [imgembed] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *image in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*help":
            const help = await getImage();
            const exampleEmbed2 = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Help')
                .setURL(help)
                .addFields({ name: 'Gif ', value: '```*gif``` Returns a random cat gif.', inline: true }, { name: 'Image ', value: '```*image``` Returns a random cat image.', inline: true }, )
                .addField('Help', '```*help```Sends this message.', true)
                .setImage(help)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [exampleEmbed2] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *help in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
    }
})

//add this function below client.on('message'
async function getGif() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', {
        headers: {
            'x-api-key': apikeys[random]
        }
    });
    return res.data[0].url;
}

async function getImage() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search', {
        headers: {
            'x-api-key': apikeys[random]
        }
    });
    return res.data[0].url;
}

//make sure this is the last line
client.login(process.env.CLIENT_TOKEN); //login to the bot using the token
