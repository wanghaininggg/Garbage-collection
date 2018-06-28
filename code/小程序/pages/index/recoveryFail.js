// pages/index/recoveryFail.js
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
  buttonFeedback: function() {
    wx.navigateTo({
      url: 'feedback'
    })
  }
})