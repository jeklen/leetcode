# leetcode
LeetCode Problems' Solutions
## 如何处理OJ的输入输出
常见的输入格式
- 预先不知道输入数据的组数
- 预先知道组数
- 只有一组数据

### 预先不输入数据的组数——读到文件结尾
C
```
while (scanf("%d%d", &a, &b) != EOF) {
printf("%d\n", a+b);
}
```
C++
```
while
