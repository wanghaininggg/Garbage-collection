// person/person.js
var app = getApp();
Page({

  data: {
      user: {}
  },
  
  onShow: function () {
   this.getData();
  },
  getData: function(){
    var _this = this;
    _this.setData({
      'user':app._user,
    });
  },
  onPullDownRefresh: function () {
    app.getUser2();
    this.getData();
    wx.stopPullDownRefresh();
  },
})