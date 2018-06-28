App({

  onLaunch: function () {
    this.getUser();
  }, 
  getUser: function(){
    var _this = this;
    _this.showLoadToast('自动登录');
    wx.login({
      success: function (res) {
        if (res.code) {
          wx.request({
            url: 'http://192.168.43.127:8000/login/',
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded' },
            data: {
              code: res.code,
            },
            success: function (res) {
              if (res.data.is_bind) {
                _this._user.we = res.data.user_info;
                _this._user.is_bind = true;
                _this._user.openid = res.data.wx_openid;
                wx.reLaunch({
                  url: '../../pages/index/index'
                })
              } else {
                _this._user.openid = res.data.wx_openid;
                wx.navigateTo({
                  url: '../../pages/person/login'
                });
              }
            }
          })
        } else {
          console.log('登录失败' + res.errMsg)
        }
      }
    });
  },
  getUser2: function () {
    var _this = this;
    wx.login({
      success: function (res) {
        if (res.code) {
          wx.request({
            url: 'http://192.168.43.127:8000/login/',
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded' },
            data: {
              code: res.code,
            },
            success: function (res) {
              if (res.data.is_bind) {
                _this._user.we = res.data.user_info;
                _this._user.is_bind = true;
                _this._user.openid = res.data.wx_openid;
              } else {
                _this._user.openid = res.data.wx_openid;
              }
            }
          })
        } else {
          console.log('登录失败' + res.errMsg)
        }
      }
    });
  },
  _user: {
    is_bind:false,
    openid: "",
    we:{}
  },

  showErrorModal: function (content, title) {
    wx.showModal({
      title: title || '加载失败',
      content: content || '未知错误',
      showCancel: false
    });
  },

  showLoadToast: function (title, duration) {
    wx.showToast({
      title: title || '加载中',
      icon: 'loading',
      duration: duration || 10000
    });
  },
})
