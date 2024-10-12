//npm install katex
const katex = require('katex'); 


const latex = 'E = mc^2';
const html = katex.renderToString(latex, {
    throwOnError: false,
});


console.log(html);
