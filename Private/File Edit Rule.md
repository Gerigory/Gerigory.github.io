文件名规范：

1. 名字要带日期，可以不是真实日期，需要按照编码格式4位-2位-2位来
2. 单词跟日期要用-分割
3. 支持中文，中文不需要分隔符
4. 不支持带有引号字符（比如单引号字符，比如Assasin's-Creed就会有问题

标题：
1. 支持中文中括号【】，不支持英文中括号[]
内容：

1. 不支持中文，有中文，会导致解析不出来？

文件夹

1. 支持中英文命名(规则同文件名)

文章缩略图：

1. 放到单独的文件夹下，似乎不行？

日期

1. 对格式有明显限制（可以只保留日期，移除时间），不符合的会影响页面的刷新！！

规则：

1. 支持新建子文件夹，文件夹名字可以使用中英文(英文需要区分大小写，文件名类似)
2. 文件名需要以日期开头，并用短横线分割，不支持空格（路径上的所有单位都不支持空格）
   - 不可以移除日期，但日期可以不是真实的
   - 日期是否可以缩写为单个数字
3. 文件名支持中文
4. 文件内容中：
   - 日期需要按照指定的格式写，格式不对会影响页面刷新：可以只保留日期
   - 标题、内容支持中文，但是注意不要添加[]，这个属于特殊字符，可以用中文的【】
   - 开头图片名字空格如何填写
5. 仓库是否可以改成私有？
6. 标题等字符串内容，支持中英文
7. 图片路径不能用明文的绝对路径，需要以{{site.baseurl}}替换“https://gerigory.github.io”?

贴图存放目录

1. 可以放到下面的子目录里，目录跟文件名不能包含空格
2. 使用的时候，可以用明文的网络绝对路径，也可以用相对路径
   1. ![]({{site.baseurl}}/assets/img/Dithering-avoids-banding/1.png)
   2. ![](https://gerigory.github.io/assets/img/Dithering-avoids-banding/1.png)
3. 格式支持各种类型，目前已测试通过的有png，jpg等

## 其他

1. 可以通过giscus来添加comment功能，参考[Commenting is Now Available Thanks to Giscus](https://www.patrickthurmond.com/blog/2023/12/11/commenting-is-available-now-thanks-to-giscus/)
