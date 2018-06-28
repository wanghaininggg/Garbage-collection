// pages/person/team.js
var app = getApp();
Page({
  data: {
    showLog: false
  },
  toggleLog: function () {
    this.setData({
      showLog: !this.data.showLog
    });
  }
});