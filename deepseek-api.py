from openai import OpenAI
import time


def call_api(api_key: str, base_url: str, content: str):
    """
    使用给定参数调用 OpenAI API，并测量 API 调用所需的时间。

    参数:
    api_key (str): 用于认证的 API 密钥。
    base_url (str): OpenAI API 的基础 URL。
    content (str): 发送到 API 的内容。

    返回:
    dict: 来自 OpenAI API 的响应。
    """

    client = OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": content},
        ],
        stream=True
    )


    return response


def stream_output(api_key: str, base_url: str, content: str):
    """
    调用 API 并流式输出响应内容。

    参数:
    api_key (str): 用于认证的 API 密钥。
    base_url (str): OpenAI API 的基础 URL。
    content (str): 发送到 API 的内容。
    """
    response = call_api(api_key, base_url, content)

    output_content = ""
    for event in response:
        if 'choices' in event and len(event['choices']) > 0:
            content_piece = event['choices'][0]['delta'].get('content', '')
            print(content_piece, end='')
            output_content += content_piece

    return output_content


if __name__ == '__main__':
    start_time = time.time()

    # 示例用法
    api_key = "sk-f56bc98f3fca4387aa05465c6d1f5568"
    base_url = "https://api.deepseek.com"
    content = "介绍一下光伏"

    print(stream_output(api_key, base_url, content))

    end_time = time.time()
    print(f"API 调用所需时间: {end_time - start_time} 秒")
