/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var anagramMappings = function(A, B) {
    var dictB = {}
    for (var i = 0; i < B.length; i++) {
        dictB[B[i]] = i
    }

    var retArr = []
    for (var i = 0; i < A.length; i++) {
        retArr.push(dictB[A[i]])
    }

    return retArr
};

/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function(str) {
    // Using toLowerCase()
    return str.toLowerCase()

    // Using ASCII
    var retStr = ""
    var lcA = "a".charCodeAt()
    var ucA = "A".charCodeAt()
    var ucZ = "Z".charCodeAt()
    var shift = lcA - ucA

    for (var i = 0; i < str.length; i++) {
        var curr = str[i].charCodeAt()
        if (ucA <= curr && curr <= ucZ) {
            retStr += String.fromCharCode(curr + shift)
        } else {
            retStr += str[i]
        }
    }
    return retStr
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    var numDict = {}

    for (var i = 0; i < nums.length; i++) {
        if (numDict.hasOwnProperty(nums[i])) {
            numDict[nums[i]]++
        } else {
            numDict[nums[i]] = 1
        }
    }

    var retArr = []
    for (var i = 1; i < nums.length + 1; i++) {
        if (numDict.hasOwnProperty(i)) {
            continue
        } else {
            retArr.push(i)
        }
    }

    return retArr
};

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
 total = 0
 var convertBST = function(root) {
     convertHelper(root)

     return root
 };

var convertHelper = function(root) {
    if (!(root)) {
        return
    }

    convertHelper(root.right)
    total += root.val
    root.val = total
    convertHelper(root.left)
}

/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    // 1 = 0b001
    // +
    // 2 = 0b010
    // =
    // 3 = 0b011

    var baseA = a.toString(2);
    var baseB = b.toString(2);
    var retArr = []


};

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    if (nums == null or nums.length == 0) {
        return 0;
    }

    for (var i = 0; i < nums.length; i++) {
        if (nums[i] >= target) {
            return i
        }
    }

    return nums.length
};
