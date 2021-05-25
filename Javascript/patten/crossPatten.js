// Print string of odd length in ‘X’ format
// Difficulty Level : Basic

inputStr = 'test_data';
let x = inputStr.length
for(let i =0; i < inputStr.length;i++){
    for(let j=0; j< inputStr.length;j++){
        if(j == 1 || j ==x)
            document.write(str.charAt(k));
        else
            document.write(" ");
    }
    document.write("<br>");
    x=x-1;
} 