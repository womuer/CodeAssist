# C/C++ Code Snippets
Vscode extension for C/C++, for easy to program.

# Github
https://github.com/womuer/CodeAssist/tree/master
## Usage
Type a part of the keywords in snippet e.g., "for" and press enter.

```c
for // Creates a for loop snippet
```
If the snippet does not appear, you can also just press <kbd>Ctrl</kbd> + <kbd>Space</kbd> (works on Windows, Linux, or Mac) to access the available snippets in the editor.


## Installation
You can  find this extension VScode extension market,  but now it's not upload in that.

1. Install Visual Studio Code
2. Launch VS Code
3. From the command palette `Ctrl`+`Shift`+`P` (Windows, Linux) or `Cmd`+`Shift`+`P` (OSX)
4. Type `ext install` or just simply select `Install Extension`
5. Choose the extension - CodeAssist Snippets
6. Relaunch VS Code

Also you can use vsix  to install this extension:
1. npm install -g @vscode/vsce
2. cd myExtension
3. vsce package
## Develop
If you want develop this extension, please also add Chinese express in snippets.
e.g: "Algo": {
    prefix": "算法",
        "body": [
            " 算法"，
        ],
        "description": "Code snippet for 算法 statement"
}
## Snippets
        for
        forr
        while
        if
        else
        else
        if
        enum
        ifdef
        ifndef
        if
        struct
        switch
        union
        inc
        inc
        def
        def
        arrBubblesort
        arrFindminarr
        arrSelectionSort
        arrQuickSort
        arrfindDuplicates
        arrFindMaxAndMin
        arrMergeSortedArrays
        arrCountElement
        arrElemSum
        arrCalculateMedian
        runStateMachine
        listRemoveNthFromEnd
        reverseBitsuint
        hammingWeight
        isValidBrackets
        bitwiseAnd
        listRemoveValElements
        listReverseList
        arrUniqueOccurrences
        arrMaxSubarray
        strIsPalindrome
        strRomanToInt
        arrSingleNumber
        listDetectCycle
        divideFindMin
        arrThreeSumClosest
        performFFT
        KalmanFilter
        arrMajorityElement
        arrMaximumUniqueSubarray
        strHalvesAreAlike
        bSTIterator
        algoMaxIceCream
        arrContainsDuplicate
        algoMaximumBags
        algominPathCost
        algoisPowerOfTwo
        isAnagram
        arrRemoveDuplicates
        arrRemoveElement
        strFindSubStr
        arrmoveZeroes
        strlengthOfLongestSubstring
        strlongestValidParentheses
        strreverseString
        arrsearchInsert
        isPerfectSquare
        algosolveSudoku
        strfirstUniqChar
        strfindTheDifference
        algotrap
        strcountSegments
        algoBFSjumpGame
        BFS
        bithammingDistance
        bitfindComplement
        floatPow
        strdetectCapitalUse
        arrayPairSum
        algotrimBST
        "compareTimeStrings",
        "compareTimeWithCurrentTime",
        "strfindStringInArray",
        "strremoveSpaces",
        "strlen",
        "strcmp",
        "sprintf",
         "timeval_addMsecs",
         "timeval_toMsecs",
         "timeval_difference",
         "timeval_add_timeval",
         "timeval_durationFromNow",

        "数组冒泡排序",
        "数组查找数组最小值",
        "数组选择排序",
        "数组快速排序",
        "数组查找重复元素",
        "数组查找最大值和最小值",
        "数组合并两个有序数组",
        "数组计数元素出现次数",
        "数组求和",
        "数组查找中位数",
        "状态机",
        "链表删除倒数第个节点",
        "位反转32",
        "求二进制1的个数",
        "检查括号配对",
        "位与",
        "链表删除给定值",
        "链表反转",
        "数组元素是否唯一",
        "数组最大子数组和",
        "字符串回文判断",
        "字符串罗马数字转int",
        "数组只出现一次的数",
        "链表存在环",
        "数组二分法查找最小值",
        "数组最接近目标的值",
        "傅里叶变换",
        "卡尔曼滤波器",
        "数组多数投票算法",
         "数组查找数组中的具有最大唯一元素和的子数组",
         "字符串前半部分和后半部分是否包含相同数量的元素",
         "二叉搜索树迭代升序遍历",
         "算法贪心算法",
         "数组是否包含重复元素",
         "算法背包的容量限制",
         "算法最短路径成本",
         "算法是否是2的幂",
         "算法字母异位词",
         "数组删除重复元素",
         "数组删除元素",
         "字符串查找字串",
          "数组将零移至数组末尾",
         "字符串最长无重复子串",
         "字符串最长括号有效子串",
         "字符串反转",
         "字符串插入查找",
         "数判断是否为完美平方",
         "算法数独问题",
         "字符串第一个不重复的元素",
         "字符串匹配",
         "算法接雨水问题",
         "字符串计算单词数",
         "算法跳跃问题",
         "二进制表示中有多少位不同",
         "补数",
         "算法浮点数幂计算",
         "字符串检查大小写",
         "数组分割查找两两配对元素最小值",
         "算法二叉搜索树修剪函数",
         "比较两个时间字符串",
         "时间字符串和当前时间作比较",
         "字符串数组中匹配字符串",
         "字符串移除空格",
         "字符串长度",
         "字符串比较",
         "时间给定时间添加毫秒",
         "时间转毫秒",
         "时间差",
         "时间两个时间相加",
         "时间与当前时间差值",

## bash Snippets

  archive compress tar.gz
  archive tar.gz
  archive compress tar.xz
  archive tar.xz
  archive compress .zip
  archive zip
  archive decompress tar.gz
  decompress tar.gz
  archive decompress tar.xz
  decompress tar.xz
  archive decompress .zip
  archive unzip
  array all
  array at index
  array concat
  array contains
  array declare
  array delete at
  array delete
  array filter
  array iterate
  array forEach
  array length
  array print
  echo array
  array push
  array add
  array slice
  array range
  array replace
  array reverse
  array set element
  command failure check
  cmd failure check
  hide command error
  don't show command error
  if command exists
  if cmd exists
  command nice
  cmd nice
  command renice
  cmd renice
  command
  cmd
  command substitution
  cmd substitution
  command success check
  cmd success check
  crypto base64 decode
  crypto base64 encode
  crypto hash
  date now dayOfMonth
  date now dayOfWeek
  date now dayOfYear
  date now short
  date now monthName
  date now monthNumber
  date now UTC
  date now year
  event CTRL+C
  event terminated
  event EXIT
  iterate directories
  directory create nested
  directory create
  directory delete nested
  directory remove nested
  file delete
  file remove
  file read
  file search
  search in files
  find in files
  file write multiline sudo
  file write multiline
  file write
  iterate files
  file find
  directory find
  if directory exists
  if file executable
  if file link
  if file exists
  if file not empty
  if file readable
  if file writeable
  if file newer
  if file older
  if file =
  if path exists
  remove old/new files/directories
  if float =
  if double =
  if float >=
  if double >=
  if float >
  if double >
  if float <=
  if double <=
  if float <
  if double <
  if float !=
  if double !=
  fn animation animate
  fn animation pacman
  fn banner color
  fn banner simple
  fn import
  fn options
  fn input choice
  fn checkbox
  fn input multichoice
  fn math average
  fn math factorial
  fn math fibonacci series
  fn math fibonacci
  fn math product
  fn math sum
  fn progress
  fn scan local
  fn time format seconds
  fn urldecode
  fn urlencode
  fn version compare
  fn semver compare
  fx animation animate
  fx animation pacman
  fx banner color
  fx banner simple
  fx import
  fx options
  fx input choice
  fx checkbox
  fx input multichoice
  fx math fibonacci
  fx math average
  fx math factorial
  fx math fibonacci series
  fx math product
  fx math sum
  fx progress
  fx scan local
  fx time format seconds
  fx urldecode
  fx urlencode
  fx version compare
  fx semver compare
  ftp delete file
  ftp download
  ftp list
  ftp rename
  ftp upload
  function arguments
  func args
  function arguments count
  func args count
  function
  func
  function return value
  func return value
  func ret val
  git branch create
  git branch delete local
  git branch delete remote
  git branch list
  git branch push
  git branch rename
  git changes revert
  git clone branch https
  git clone branch
  git clone https
  git clone
  git commit list notPushed
  git commit search
  git commit undo
  git commit
  git config list
  git config set
  git patch apply
  git patch create
  git remote list
  git remote urlAdd https
  git remote url add https
  git remote urlAdd
  git remote url add
  git remote urlAdd ssh
  git remote url add ssh
  git remote urlChange https
  git remote url change https
  git remote urlChange
  git remote url change
  git remote urlChange ssh
  git remote url change ssh
  git tag commit
  git commit tag
  git tag list
  git tag remote delete
  git tag remote push
  http cookie
  http download
  http GET
  http DELETE
  http header
  http POST file
  http POST
  http PUT
  input password
  input text
  ask question
  if int =
  if int >=
  if int >
  if int <=
  if int <
  if int !=
  for ij
  for i
  for in collection
  for in column
  for in range
  if
  iff not
  iff
  loop infinite
  switch case
  loop until
  loop while
  ip local IPs
  ip info
  ip public
  math +
  math const 𝛾
  math const e
  math const Ω
  math const ϕ
  math const π
  math --
  math /=
  math /
  expr
  arithmetic
  math ++
  let
  math -=
  math %=
  math %
  math *=
  math *
  math +=
  math ^
  math 0.00
  math random
  math √
  math sqrt
  math -
  am I not root
  am I not sudo
  am I root
  am I sudo
  animation frame
  argument parsing
  parse args
  echo text
  print text
  echo variable
  print variable
  exit code
  os is
  region
  section
  shebang
   
  first line
  sleep
  stopwatch elapsed
  stopwatch start
  stopwatch stop
  summary
  timeout
  color black
  color blue
  color cyan
  color green
  color magenta
  color red
  color white
  color yellow
  format bold
  format dim
  format italic
  format reverse
  process ID(s)
  process instances
  process kill
  process list all
  process Name by ID
  string concat
  string + string
  string contains
  if string contains
  string indexOf
  if string empty
  if string =
  string equal
  if string not empty
  if string !=
  string not equal
  string length
  string random
  string replace
  string reverse
  string substring count
  string substring frequency
  string substring
  string toLower
  string toUpper
  string trim all
  string trim left
  string trim right
  string trim
  system distro codename
  system distro name
  system distro version
  system kernel name
  system kernel release
  system memory info
  system processor architecture
  system cpu architecture
  system cpu arch
  system processor count
  system cpu count
  system processor model
  system cpu model
  system processor type
  system cpu type
  service manage
  systemd manage
  system uptime seconds
  system uptime
  time seconds epoch
  time now local
  time now UTC
  variable assign
  variable set
  variable default value
  assign if empty
  var
  variable read
  variable expand





