function solution(num_list) {
    var answer = 0;
    var odd = ''; var even = '';
    
    for (const num of num_list) {
        if (num % 2 == 0)
            even += num;
        else odd += num;
    }
    
    answer = Number(odd) + Number(even)
    return answer;
}