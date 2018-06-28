// pages/index/recoverySuccess.js
Page({

  onLoad: function (options) {
    this.setData({
      message: options.message
    });
  },
  buttonReturn: function () {
    wx.navigateBack({
    });
  },
})