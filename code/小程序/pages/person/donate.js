// pages/person/donate.js
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
  },
  onShow: function () { 
    var credit = app._user.we.credit;
    var _this = this;
    wx.request({
      url: 'http://192.168.43.127:8000/denote/',
      success: function (res) {
        console.log(res.data);
        _this.setData({
          totalCredit: res.data,
        });
      }
    });
  } ,
  formSubmit: function (e) {
    if (parseInt(e.detail.value.input.trim()) > 0){

      wx.request({
        url: 'http://192.168.43.127:8000/denote/',
        method: 'post',
        data: {
          user: app._user.we.number,
          num: e.detail.value.input,
        },
        header: { 'content-type': 'application/x-www-form-urlencoded' },
        success: function (res) {
          if(res.data.status){
            wx.navigateTo({
              url: 'success'
            })
          }else{
            wx.showToast({
              title: res.data.message,
              icon: 'none',
              duration: 2000
            })
          }
        }
      })
    }else{
      wx.showToast({
        title: '请输入正确的捐赠额度',
        icon: 'none',
        duration: 2000
      })
    }
  },
})