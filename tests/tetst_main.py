import unittest

from hicon import extract


class MainTestCase(unittest.IsolatedAsyncioTestCase):
    """测试主要功能
    TODO https://docs.python.org/zh-cn/3/library/unittest.html#unittest.IsolatedAsyncioTestCase.run # noqa
    """
    async def test_extract(self):
        """测试 main.extract 功能"""
        result = await extract('https://news.ifeng.com/c/8a0ytPBvYg6')
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get('title'), '缺少必要的title')


if __name__ == '__main__':
    unittest.main()
