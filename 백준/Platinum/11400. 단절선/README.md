# [Platinum IV] 단절선 - 11400 

[문제 링크](https://www.acmicpc.net/problem/11400) 

### 성능 요약

메모리: 14424 KB, 시간: 148 ms

### 분류

그래프 이론, 그래프 탐색, 깊이 우선 탐색, 단절점과 단절선

### 제출 일자

2025년 7월 26일 20:33:37

### 문제 설명

<p>그래프가 주어졌을 때, 단절선을 모두 구해 출력하는 프로그램을 작성하시오.</p>

<p>단절선이란 그 간선을 제거했을 때, 그래프가 두 개 또는 그 이상으로 나누어지는 간선을 말한다. 즉, 제거했을 때 그래프의 connected component의 개수가 증가하는 간선을 말한다.</p>

### 입력 

 <p>첫째 줄에 두 정수 V(1≤V≤100,000), E(1≤E≤1,000,000)가 주어진다. 이는 그래프가 V개의 정점과 E개의 간선으로 이루어져 있다는 의미이다. 다음 E개의 줄에는 간선에 대한 정보를 나타내는 두 정수 A, B가 주어진다. 이는 A번 정점과 B번 정점이 연결되어 있다는 의미이며, 방향은 양방향이다.</p>

<p>그래프는 항상 연결되어 있으며, 같은 간선이 두 번 이상 들어오는 경우는 없다. 또, A와 B가 같은 경우도 없다.</p>

<p>그래프의 정점은 1부터 V까지 자연수이다.</p>

### 출력 

 <p>첫째 줄에 단절선의 개수 K를 출력한다.</p>

<p>둘째 줄부터 K개 줄에는 단절선을 사전순으로 한 줄에 하나씩 출력한다. 간선은 "A B" 형식으로 출력해야 하고, A < B를 만족해야 한다. 같은 간선은 한 번만 출력하면 된다. 즉, "A B"를 출력한 경우에 "B A"는 출력할 필요가 없다.</p>

