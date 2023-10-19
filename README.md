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
bash archive compress tar.gz
bash archive tar.gz
bash archive compress tar.xz
bash archive tar.xz
bash archive compress .zip
bash archive zip
bash archive decompress tar.gz
bash decompress tar.gz
bash archive decompress tar.xz
bash decompress tar.xz
bash archive decompress .zip
bash archive unzip
bash array all
bash array at index
bash array concat
bash array contains
bash array declare
bash array delete at
bash array delete
bash array filter
bash array iterate
bash array forEach
bash array length
bash array print
bash echo array
bash array push
bash array add
bash array slice
bash array range
bash array replace
bash array reverse
bash array set element
bash command failure check
bash cmd failure check
bash hide command error
bash don't show command error
bash if command exists
bash if cmd exists
bash command nice
bash cmd nice
bash command renice
bash cmd renice
bash command
bash cmd
bash command substitution
bash cmd substitution
bash command success check
bash cmd success check
bash crypto base64 decode
bash crypto base64 encode
bash crypto hash
bash date now dayOfMonth
bash date now dayOfWeek
bash date now dayOfYear
bash date now short
bash date now monthName
bash date now monthNumber
bash date now UTC
bash date now year
bash event CTRL+C
bash event terminated
bash event EXIT
bash iterate directories
bash directory create nested
bash directory create
bash directory delete nested
bash directory remove nested
bash file delete
bash file remove
bash file read
bash file search
bash search in files
bash find in files
bash file write multiline sudo
bash file write multiline
bash file write
bash iterate files
bash file find
bash directory find
bash if directory exists
bash if file executable
bash if file link
bash if file exists
bash if file not empty
bash if file readable
bash if file writeable
bash if file newer
bash if file older
bash if file =
bash if path exists
bash remove old/new files/directories
bash if float =
bash if double =
bash if float >=
bash if double >=
bash if float >
bash if double >
bash if float <=
bash if double <=
bash if float <
bash if double <
bash if float !=
bash if double !=
bash fn animation animate
bash fn animation pacman
bash fn banner color
bash fn banner simple
bash fn import
bash fn options
bash fn input choice
bash fn checkbox
bash fn input multichoice
bash fn math average
bash fn math factorial
bash fn math fibonacci series
bash fn math fibonacci
bash fn math product
bash fn math sum
bash fn progress
bash fn scan local
bash fn time format seconds
bash fn urldecode
bash fn urlencode
bash fn version compare
bash fn semver compare
bash fx animation animate
bash fx animation pacman
bash fx banner color
bash fx banner simple
bash fx import
bash fx options
bash fx input choice
bash fx checkbox
bash fx input multichoice
bash fx math fibonacci
bash fx math average
bash fx math factorial
bash fx math fibonacci series
bash fx math product
bash fx math sum
bash fx progress
bash fx scan local
bash fx time format seconds
bash fx urldecode
bash fx urlencode
bash fx version compare
bash fx semver compare
bash ftp delete file
bash ftp download
bash ftp list
bash ftp rename
bash ftp upload
bash function arguments
bash func args
bash function arguments count
bash func args count
bash function
bash func
bash function return value
bash func return value
bash func ret val
bash git branch create
bash git branch delete local
bash git branch delete remote
bash git branch list
bash git branch push
bash git branch rename
bash git changes revert
bash git clone branch https
bash git clone branch
bash git clone https
bash git clone
bash git commit list notPushed
bash git commit search
bash git commit undo
bash git commit
bash git config list
bash git config set
bash git patch apply
bash git patch create
bash git remote list
bash git remote urlAdd https
bash git remote url add https
bash git remote urlAdd
bash git remote url add
bash git remote urlAdd ssh
bash git remote url add ssh
bash git remote urlChange https
bash git remote url change https
bash git remote urlChange
bash git remote url change
bash git remote urlChange ssh
bash git remote url change ssh
bash git tag commit
bash git commit tag
bash git tag list
bash git tag remote delete
bash git tag remote push
bash http cookie
bash http download
bash http GET
bash http DELETE
bash http header
bash http POST file
bash http POST
bash http PUT
bash input password
bash input text
bash ask question
bash if int =
bash if int >=
bash if int >
bash if int <=
bash if int <
bash if int !=
bash for ij
bash for i
bash for in collection
bash for in column
bash for in range
bash if
bash iff not
bash iff
bash loop infinite
bash switch case
bash loop until
bash loop while
bash ip local IPs
bash ip info
bash ip public
bash math +
bash math const 𝛾
bash math const e
bash math const Ω
bash math const ϕ
bash math const π
bash math --
bash math /=
bash math /
bash expr
bash arithmetic
bash math ++
bash let
bash math -=
bash math %=
bash math %
bash math *=
bash math *
bash math +=
bash math ^
bash math 0.00
bash math random
bash math √
bash math sqrt
bash math -
bash am I not root
bash am I not sudo
bash am I root
bash am I sudo
bash animation frame
bash argument parsing
bash parse args
bash echo text
bash print text
bash echo variable
bash print variable
bash exit code
bash os is
bash region
bash section
bash shebang
bash bash
bash first line
bash sleep
bash stopwatch elapsed
bash stopwatch start
bash stopwatch stop
bash summary
bash timeout
bash color black
bash color blue
bash color cyan
bash color green
bash color magenta
bash color red
bash color white
bash color yellow
bash format bold
bash format dim
bash format italic
bash format reverse
bash process ID(s)
bash process instances
bash process kill
bash process list all
bash process Name by ID
bash string concat
bash string + string
bash string contains
bash if string contains
bash string indexOf
bash if string empty
bash if string =
bash string equal
bash if string not empty
bash if string !=
bash string not equal
bash string length
bash string random
bash string replace
bash string reverse
bash string substring count
bash string substring frequency
bash string substring
bash string toLower
bash string toUpper
bash string trim all
bash string trim left
bash string trim right
bash string trim
bash system distro codename
bash system distro name
bash system distro version
bash system kernel name
bash system kernel release
bash system memory info
bash system processor architecture
bash system cpu architecture
bash system cpu arch
bash system processor count
bash system cpu count
bash system processor model
bash system cpu model
bash system processor type
bash system cpu type
bash service manage
bash systemd manage
bash system uptime seconds
bash system uptime
bash time seconds epoch
bash time now local
bash time now UTC
bash variable assign
bash variable set
bash variable default value
bash assign if empty
bash var
bash variable read
bash variable expand






