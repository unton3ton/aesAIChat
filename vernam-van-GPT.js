function vernamCipher(input, key) {
  if (key.length < input.length) {
    key = generateKey(input.length);
  }
  var output = '';
  for (var i = 0; i < input.length; i++) {
    output += String.fromCharCode(input.charCodeAt(i) ^ key.charCodeAt(i % key.length));
  }
  return output;
}

function generateKey(length) {
  var key = '';
  for (var i = 0; i < length; i++) {
    key += String.fromCharCode(getRandomInt(0, 66535));
  }
  return key;
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

// пример использования
// var input = prompt("Введите исходный текст");
// var key = prompt("Введите ключ");
// var output = vernamCipher(input, key);
// console.log("Зашифрованный текст:", output);

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Введите исходный текст: ', (input) => {
  rl.question('Введите ключ шифрования: ', (key) => {
    var output = vernamCipher(input, key);
    console.log('Зашифрованный текст:', output);
    rl.close();
  });
});

// Введите исходный текст: oki
// Введите ключ шифрования: doki
// Зашифрованный текст: ♂♦☻

// C:\Users\Peter\Desktop>node vernam-van-GPT.js
// Введите исходный текст: okki
// Введите ключ шифрования: doki
// Зашифрованный текст: ♂♦