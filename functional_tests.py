from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #(1)
    def setUp(self):       #(3) 测试执行前
        self.browser = webdriver.Firefox()

    def tearDown(self):    #(3) 测试方法执行后
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):    #(2) 测试方法
        # 乔伊听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部包含'To-Do'这个词
        self.assertIn('To-Do',self.browser.title)           #(4) 测试失败执行
        self.fail('Finish the test!')  #(5)

        # 应用邀请她输入一个待办事项

        # 她在文本中输入了'Buy peacock feathers'（购买孔雀羽毛）
        # 她的爱好是钓鱼

        # 她输入回车键后页面刷新了
        # 待办事项显示'1：Buy peacock feathers'

        # 页面又显示了一个文本框，可以输入其他待办事项
        # 她输入了'Use peacock feathers to make a fly'(做假蝇)
        # 她做事非常有条理

        # 页面再次刷新，她的清单显示两条事项

        # 她想知道这个网站是否会记住她的清单
        # 她看到网站为她生成了一个唯一的URL
        # 而且页面中有一个文字解说这个功能

        # 她访问那个URL，发现她的清单还在

        # 她很满意，去休息了

if __name__ == '__main__': #(6)
    unittest.main(warnings='ignore')    #(7)禁止抛出ResourceWarning