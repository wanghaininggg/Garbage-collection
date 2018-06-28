// pages/index/feedback.js
var app = getApp();
Page({

  formSubmit: function(e){
   console.log(e.detail.value.information)
   if(e.detail.value.information.trim){
     wx.request({
       url: 'http://192.168.43.127:8000/feedback/',
       method: 'post',
       data: {
         user: app._user.we.number,
         information: e.detail.value.information.trim(),
       },
       header: { 'content-type': 'application/x-www-form-urlencoded' },
       success: function (res) {
         wx.navigateTo({
           url: 'recoverySuccess?message=' + "谢谢您的反馈，我们会努力改进"
         })
       }
     })
   }
  }
})