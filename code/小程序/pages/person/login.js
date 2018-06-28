var app = getApp();
Page({
  data: {
    remind: '加载中',
    userid_focus: false,
    passwd_focus: false,
    userid: '',
    passwd: '',
    angle: 0
  },
  onReady: function () {
    var _this = this;
    setTimeout(function () {
      _this.setData({
        remind: ''
      });
    }, 1000);
  },
  bind: function () {
    var _this = this;
    if (!_this.data.userid || !_this.data.passwd) {                 
      app.showErrorModal('账号及密码不能为空', '提醒');
      return false;
    }
    app.showLoadToast('绑定中');
    wx.request({
      method: 'POST',
      header: { 'content-type': 'application/x-www-form-urlencoded' },
      url: 'http://192.168.43.127:8000/bind/',
      data: {
        openid: app._user.openid,
        yktid: _this.data.userid,
        passwd: _this.data.passwd
      },
      success: function (res) {
        if (res.data.status == true) {
          app.showLoadToast('请稍候');
          
            wx.showToast({
              title: '绑定成功',
              icon: 'success',
              duration: 1500
            });
            app.getUser();
        } else {
          wx.hideToast();
          app.showErrorModal(res.data.message, "绑定失败");
        }
      },
      fail: function (res) {
        wx.hideToast();
        app.showErrorModal(res.errMsg, '绑定失败');
      }
    });
  },
  useridInput: function (e) {
    this.setData({
      userid: e.detail.value
    });
    if (e.detail.value.length >= 10) {
      wx.hideKeyboard();
    }
  },
  passwdInput: function (e) {
    this.setData({
      passwd: e.detail.value
    });
  },
  inputFocus: function (e) {
    if (e.target.id == 'userid') {
      this.setData({
        'userid_focus': true
      });
    } else if (e.target.id == 'passwd') {
      this.setData({
        'passwd_focus': true
      });
    }
  },
  inputBlur: function (e) {
    if (e.target.id == 'userid') {
      this.setData({
        'userid_focus': false
      });
    } else if (e.target.id == 'passwd') {
      this.setData({
        'passwd_focus': false
      });
    }
  },
});