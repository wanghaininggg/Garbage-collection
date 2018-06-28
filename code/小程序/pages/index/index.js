// index/index.js
var app = getApp();
Page({
  data: {
    user:{},
  },
  onShow:function(){
    var _this = this;
    _this.setData({
      'user': app._user,
    });
  },
  use: function(){
    var id = app._user.we.number;
    wx.chooseImage({
      sizeType: ['compressed'],
      sourceType: ['album', 'camera'],
      success: function (res) {
        var tempFilePaths = res.tempFilePaths;
        app.showLoadToast('上传处理中', 15000);
        wx.uploadFile({
          url: 'http://192.168.43.127:8000/index/',
          filePath: tempFilePaths[0],
          name: 'file',
          formData: {
            userId: id,
          },
          success: function (res) {
            var a = JSON.parse(res.data);
            wx.hideToast();
            console.log(a);
            if (a.status == true){
              wx.navigateTo({
                url: 'recoverySuccess?message='+a.message
              })
            }else{
              wx.navigateTo({
                url: 'recoveryFail?message=' + a.message
              })
            }
          },
          fail: function (res) {
            wx.showToast({
              title: '上传失败',
              icon: 'none',
              duration: 2000
            })
          }
        })
      }
    })
  },
})