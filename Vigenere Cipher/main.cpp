#include <iostream>
using namespace std;

void Encryption(string plain_text, string key, string cipher_text){
    
    int x;
    cout << ">>> Encrypting the message <<<" << endl;
    for (x = 0; x < plain_text.length(); x ++){
        char a = ( plain_text[x] + key[x % key.length()] ) % 26;
        a += 'A';
        cipher_text.push_back(a);
    }
    cout << "Cipher Text : " << cipher_text << endl;
    
}

void Decryption(string plain_text, string key, string cipher_text){
    
    int y;
    cout << ">>> Decrypting the message <<<" << endl;
    for (y = 0; y < cipher_text.length(); y ++){
        char b = ( cipher_text[y] - key[y % key.length()] + 26) % 26;
        b += 'A';
        plain_text.push_back(b);
    }
    cout << "Plain Text : " << plain_text << endl;
    
}

int main(){
    string plain_text, key, cipher_text;
    
    int choice;
    cout << "-----  Vigenere Cipher  -----" << endl;
    while(true){
        
        cipher_text = "";
        plain_text = "";
        key = "";
        
        cout << "1. Encryption" << endl;
        cout << "2. Decryption" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your option : ";
        cin >> choice;
        
        if (choice == 1) {
            
            cout << "Enter the Plain Text : ";
            cin >> plain_text;
            cout << "Enter the Key : ";
            cin >> key;
            Encryption(plain_text, key, cipher_text);
            
        }
        
        else if (choice == 2) {
            
            cout << "Enter the Cipher Text : ";
            cin >> cipher_text;
            cout << "Enter the Key : ";
            cin >> key;
            Decryption(plain_text, key, cipher_text);
            
        }
        
        else {
            exit(0);
        }

    }
}
