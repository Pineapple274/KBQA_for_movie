<template lang="pug">
#app
  VueBotUI(
    :options="botOptions",
    :messages="messageData",
    :bot-typing="botTyping",
    :input-disable="inputDisable",
    :is-open="false",
    @init="botStart",
    @msg-send="msgSend",
  )
</template>
<script>
import BotIcon from './assets/icons/bot.png'
import { VueBotUI } from './vue-bot-ui'
import { messageService } from './helpers/message'
import axios from "axios";

export default {
  components: {
    BotIcon,
    VueBotUI
  },

  data () {
    return {
      apiEndpoint: "http://127.0.0.1:5000/query",
      messageData: [],
      botTyping: false,
      inputDisable: false,
      botOptions: {

        botTitle: "影视咨询",
        botAvatarImg: BotIcon,
        boardContentBg: '#f4f4f4',
        msgBubbleBgBot: '#fff',
        inputPlaceholder: 'Type hereeee...',
        inputDisableBg: '#fff',
        inputDisablePlaceholder: 'Hit the buttons above to respond'
      }
    }
  },

  methods: {
    botStart () {
      // Get token if you want to build a private bot
      // Request first message here

      // Fake typing for the first message
      this.botTyping = true;
      setTimeout(() => {

        this.botTyping = false;
        this.messageData.push({
          agent: 'bot',
          type: 'text',
          text: 'Hi，欢迎咨询'
        });
      }, 1000);
    },

    msgSend (value) {
      // Push the user's message to board
      this.messageData.push({
        agent: 'user',
        type: 'text',
        text: value.text
      });

     // this.getResponse(value);
    //},

    // Submit the message from user to bot API, then get the response from Bot
    //getResponse (data) {
      // Loading
      this.botTyping = true;
      this.inputDisable = true;

      // Post the message from user here
      // Then get the response as below

      // Create new message from fake data
      axios.post(this.apiEndpoint, { "question": value.text }).then((response) => {
        console.log(response);

        this.messageData.push({
          agent: "bot",
          type: "text",
          text: response.data.answer
        });
      });
      this.botTyping = false;
      this.inputDisable = false;
    },
  }
}
</script>
<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
