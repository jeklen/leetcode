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
while (cin>>a>>b) {
	cout << a + b << endl;
}
```
java
```
Scanner scanner = new Scanner(System.in);
while (scanner.hasNextInt()) {
	int a = scanner.nextInt();
	int b = scanner.nextInt();
	System.out.println(a+b);
}
```

### 预先知道数据组数--读数据组数然后循环
C
```
scanf("%d", &n);
for (int i = 0; i<n; i++) {
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a+b);
}
```
C++
```
cin >> n;
for (int i=0; i<n; i++) {
	int a, b;
	cin >> a >> b;
	cout << a+b << endl;
}
```
java
```
Scanner scanner = new Scanner(System.in);
int n = scanner.nextInt();
for (int i=0; i<n; i++) {
	int a = scanner.nextInt();
	int b = scanner.nextInt();
	System.out.println(a+b);
}
```

### 只有一组数据---直接读
C
```
scanf("%d%d", &a&b);
printf(%d\n", a+b);
```
C++
```
cin >> a >> b;
cout << a+b << endl;
```
java
```
int a = scanner.nextInt();
int b = scanner.nextInt();
```

## 处理输出格式

### 不用输出case数
C
```
scanf("%d%d", &n);
for (int i = 0; i<n; i++) {
	int a, b;
	scanf("%d%d", &a, &b);
	printf("%d\n", a+b);
}
```
C++
```
cin >> n;
for (int i = 0; i<n; i++) {
	int a, b;
	cin >> a >> b;
	cout << a+b << endl;
}
```
java
```
Scanner scanner = new Scanner(System.in);
int n = scanner.nextInt();
for (int i=0; i<n; i++) {
	int a = scanner.nextInt();
	int b = scanner.nextInt();
	System.out.println(a+b);
}
```
