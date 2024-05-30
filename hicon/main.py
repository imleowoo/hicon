import asyncio
from argparse import ArgumentParser
from pprint import pprint

from gne import GeneralNewsExtractor
from pyppeteer import launch


async def page_content(url: str, headless: bool = True) -> str:
    """获取浏览器网页源代码

    :param url: 需要获取的页面URL
    :type url: str
    :param headless: 浏览器是否开启无头
    :type headless: bool

    """
    browser = await launch(headless=headless)
    try:
        page = await browser.newPage()
        await page.goto(url)
        return await page.content()
    finally:
        await browser.close()


async def main():
    parser = ArgumentParser('通过URL获取正文信息')
    parser.add_argument('url', type=str, help='需要提取正文的页面URL')
    parser.add_argument('--browser-headless', type=bool, default=1, help='浏览器是否无头')
    args = parser.parse_args()
    # content = await page_content('https://news.ifeng.com/c/8ZgrBRofRh3')
    content = await page_content(url=args.url, headless=args.browser_headless)
    extractor = GeneralNewsExtractor()
    result = extractor.extract(content)
    pprint(result)
    return result


if __name__ == '__main__':
    asyncio.run(main())
