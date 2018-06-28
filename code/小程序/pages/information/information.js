// pages/information/information.js
var app = getApp();
Page({
  data: {
    tabs: ["历史记录", "排名"],
    activeIndex: 0,
    sliderOffset: 0,
    sliderLeft: 0,
    user: app._user,
    information: [],
    rank:[],
  },
  onShow: function () {
    var id = app._user.we.number;
    var _this =this;
    wx.request({
      url: 'http://192.168.43.127:8000/history/',
      method: 'POST',
      header: { 'content-type': 'application/x-www-form-urlencoded' },
      dataType: 'json',
      data: {
        userId: id,
      },
      success: function (res) {
        _this.setData({
          information: res.data,
        });
      }
    });
    wx.request({
      url: 'http://192.168.43.127:8000/rank/',
      success: function (res) {
        // console.log(res.data)
        _this.setData({
          rank: res.data,
        });
      }
    });
  },
  tabClick: function (e) {
    this.setData({
      sliderOffset: e.currentTarget.offsetLeft,
      activeIndex: e.currentTarget.id
    });
  }
});