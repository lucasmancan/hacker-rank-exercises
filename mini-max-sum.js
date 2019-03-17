'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the miniMaxSum function below.
function miniMaxSum(arr) {
    let maxValue = arr[0];
    let minValue = arr[0];
    let sum =0;

    for (let i = 0; i < arr.length; i++){
        sum += arr[i];
        if (arr[i] > maxValue) maxValue = arr[i];
        if (arr[i] < minValue) minValue = arr[i];
    } 

    console.log(sum - maxValue, sum - minValue);
}

function main() {
    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

    miniMaxSum(arr);
}
