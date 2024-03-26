"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      messages: [
        {
          id: 1,
          text: "你好！1233333333333333333333333333333333333333333333333333",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 1,
          text: "你好！",
          isMine: false
        },
        {
          id: 2,
          text: "嗨，你好！",
          isMine: true
        },
        {
          id: 3,
          text: "嗨，你好！",
          isMine: false
        },
        {
          id: 4,
          text: "嗨，你好！",
          isMine: true
        }
      ],
      newMessage: ""
    };
  },
  methods: {
    sendMessage: function() {
      if (this.newMessage.trim()) {
        const id = this.messages.length + 1;
        this.messages.push({
          id,
          text: this.newMessage,
          isMine: true
        });
        this.newMessage = "";
      }
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: common_vendor.f($data.messages, (message, k0, i0) => {
      return {
        a: common_vendor.t(message.text),
        b: message.isMine ? 1 : "",
        c: message.id
      };
    }),
    b: common_vendor.o((...args) => $options.sendMessage && $options.sendMessage(...args)),
    c: common_vendor.o((...args) => $options.sendMessage && $options.sendMessage(...args)),
    d: $data.newMessage,
    e: common_vendor.o(($event) => $data.newMessage = $event.detail.value)
  };
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render], ["__file", "D:/dfrj/miniapp/pages/invoke/invoke.vue"]]);
wx.createPage(MiniProgramPage);
