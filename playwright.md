# Playwright 网络请求处理方法总结



<!-- 使用 page.route 可以在请求发送之前拦截和修改请求，适用于需要修改请求或提供自定义响应的场景。
使用 page.on('response') 可以在请求完成后处理响应，适用于需要读取和处理响应内容的场景。 -->


## `page.route`

用于拦截和修改网络请求。

### 功能
- 在请求发送之前拦截和修改请求。
- 可以修改请求的 URL、头信息、方法等。
- 可以选择阻止请求、继续请求或提供自定义响应。

### 示例

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # 拦截 /api 请求
        await page.route('**/api/**', lambda route, request: asyncio.create_task(handle_request(route, request)))

        # 监听响应事件
        page.on('response', handle_response)

        # 打开页面
        await page.goto('https://example.com')

        # 其他操作...

        # 关闭浏览器
        await browser.close()

async def handle_request(route, request):
    print(f"Intercepted request to: {request.url()}")
    # 你可以在这里修改请求或响应
    await route.continue()

async def handle_response(response):
    if '/api' in response.url:
        print(f"Intercepted response from: {response.url}")
        # 你可以在这里处理响应，例如获取响应内容
        content = await response.text()
        print(f"Response content: {content}")

asyncio.run(main())