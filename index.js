require('dotenv').config();
const Discord = require('discord.js');
const axios = require('axios');
const { MessageEmbed } = require('discord.js');
const token = process.env['token']
const client = new Discord.Client({ intents: ["GUILDS", "GUILD_MESSAGES"] })
const apikeys = ["put-api-key-here", "put-api-key-here"];
const random = Math.floor(Math.random() * apikeys.length);

client.on('ready', () => {
    rpc();
    console.log(`Logged in as ${client.user.tag}!`);
    console.log();
    console.log('Logs:');
});

// message events
client.on('messageCreate', async msg => {
    switch (msg.content) {
        case "*gif":
            const gif = await getGif(); //fetches a URL from the API
            const gifembed = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat gif:')
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
                .setImage(img)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [imgembed] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *image in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*fact":
            const fact = await getFact();
            const factimg = await getImage();
            const factembed = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Here\'s your cat fact:')
                .setDescription(fact)
                .setImage(factimg)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [factembed] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *fact in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
        case "*help":
            const help = await getImage();
            const help2 = new MessageEmbed()
                .setColor('#0099ff')
                .setTitle('Help')
                .addFields({ name: 'Gif ', value: '```*gif``` Returns a random cat gif.', inline: false }, { name: 'Image ', value: '```*image``` Returns a random cat image.', inline: false }, { name: 'Fact ', value: '```*fact``` Returns a cat fact.', inline: false }, { name: 'Help ', value: '```*help```Sends this message.', inline: false } )
                .setImage(help)
                .setFooter({ text: 'Made by @gifkitties', iconURL: 'https://cdn.discordapp.com/attachments/889397754458169385/985133240098627644/ezgif-3-df748915d9.gif' });
            msg.channel.send({ embeds: [help2] });
            console.log('User: ' + msg.author.tag + ' ID: ' + msg.author.id + ' ran *help in Channel: #' + msg.channel.name + ' Server: ' + msg.guild.name)
            break;
    }
})

//functions
async function getGif() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', {
        headers: {
            'x-api-key': apikeys[random]
        }
    });
    return res.data[0].url;
}

async function getImage() {
    const res = await axios.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png', {
        headers: {
            'x-api-key': apikeys[random]
        }
    });
    return res.data[0].url;
}

async function getFact() {
    const util = require("util");
    const fs = require("fs");
    const readFile = util.promisify(fs.readFile);
    const fileContent = await readFile("catfact.txt", "utf-8");
    var lines = fileContent.split("\n");
    var randLineNum = Math.floor(Math.random() * lines.length);
    return(lines[randLineNum]);
}

//updates rpc every 15 sec
async function rpc() {
    client.user.setActivity(`*help in ${client.guilds.cache.size} Servers `, { type: "LISTENING" })
    setTimeout(rpc, 15000); // change value for rpc update interval, currently at 15 seconds
}

client.login(token); //login to the bot using the token

