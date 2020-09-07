# coding=utf-8

import os
import sys

fileName = input('input the model name: ')


# step1 创建文件夹
folder = './' + fileName
if os.path.exists(folder) is False:
    os.mkdir(folder)
os.chdir(folder)  # 进入文件夹

# step2 创建index.js
jsFile = fileName + '.js'
jsContent = '''
// %s

const util = require('../../utils/util.js')

//获取应用实例
const app = getApp()

Page({

      /**
       * 页面的初始数据
       */
      data: {
    
      },
    
      /**
       * 生命周期函数--监听页面加载
       */
      onLoad: function (options) {
    
      },
    
      /**
       * 生命周期函数--监听页面初次渲染完成
       */
      onReady: function () {
    
      },
    
      /**
       * 生命周期函数--监听页面显示
       */
      onShow: function () {
    
      },
    
      /**
       * 生命周期函数--监听页面隐藏
       */
      onHide: function () {
    
      },
    
      /**
       * 生命周期函数--监听页面卸载
       */
      onUnload: function () {
    
      },
    
      /**
       * 页面相关事件处理函数--监听用户下拉动作
       */
      onPullDownRefresh: function () {
    
      },
    
      /**
       * 页面上拉触底事件的处理函数
       */
      onReachBottom: function () {
    
      },
    
      /**
       * 用户点击右上角分享
       */
      onShareAppMessage: function () {
    
      }
})
''' % jsFile
file1 = open(jsFile, 'w+')
file1.write(jsContent)
file1.flush()
file1.close()



# step3 创建index.json
jsFile3 = fileName + '.json'
jsContent3 = '''
{
    "navigationBarTitleText": "标题",
    "usingComponents": {},
    "backgroundTextStyle": "dark",
    "enablePullDownRefresh": true,
    "onReachBottomDistance": 50
}
'''
file3 = open(jsFile3, 'w+')
file3.write(jsContent3)
file3.flush()
file3.close()


# step4 创建index.wxml
jsFile4 = fileName + '.wxml'
jsContent4 = '''
<view class="container">
    
    
</view>

'''
file4 = open(jsFile4, 'w+')
file4.write(jsContent4)
file4.flush()
file4.close()

# step5 创建index.wxss
jsFile5 = fileName + '.wxss'
jsContent5 = '''
page {
    background: #f6f6f6;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

'''
file5 = open(jsFile5, 'w+')
file5.write(jsContent5)
file5.flush()
file5.close()

print(sys.argv[0])

