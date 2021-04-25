
import requests
import parsel




url = 'https://mikanani.me/Home/Classic'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


response = requests.get(url=url,headers=headers)
html_data = response.text
print(html_data)


selector = parsel.Selector(html_data)
a_s = selector.xpath('//tbody/tr/td[3]/a[1]/@href').getall()
print(a_s)

for a in a_s:
    all_url = 'https://mikanani.me' + a
    print(all_url)
    
    response_2 = requests.get(url=all_url,headers=headers).text
    selector_2 = parsel.Selector(response_2)
    
    source_title = selector_2.xpath('//p[@class="episode-title"]/text()').get()
    source_url = selector_2.xpath('//div[@class="leftbar-nav"]/a[1]/@href').get()
   # print(source_title,source_url)
    
    source_data = requests.get(url='https://mikanani.me'+source_url,headers=headers).content

# 保存文件
     file_name = source_url.split('/')[-1]
     with open(file_name,mode='wb') as f:
        f.write(source_data)
        print('资源下载完成',source_title)