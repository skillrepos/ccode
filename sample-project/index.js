// Sample JavaScript file with intentional issues for Lab 3
function calculate_sum(a, b) {
    return a + b
}

function findMax(numbers) {
    let max = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] > max)
            max = numbers[i];
    }
    return max;
}

console.log("Sample application ready!");
