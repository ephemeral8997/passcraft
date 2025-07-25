# passcraft  
  
🔐 A secure, customizable password generator for the command line.   
  
---  
  
## 🚀 Features  
  
- ✅ Adjustable password **length**  
- 🔤 Include or exclude **letters, digits, symbols**  
- 🚫 Exclude specific **ambiguous characters** (`0OIl1`)  
- 📋 Copy to **clipboard** (optional, via `pyperclip`)  
- 🧠  Display password **entropy** (bits of strength)  
- 💥 CLI-first, script-friendly, no external config files  
  
---  
  
## 📦 Requirements  
  
- Python **3.6+**  
- Optional: [`pyperclip`](https://pypi.org/project/pyperclip/) for clipboard support  
  
Install clipboard support:  
```bash  
pip install pyperclip  
```  
  
---  
  
## 🧪 Usage  
  
Run the script from the command line:  
  
```bash  
python passcraft.py [options]  
```  
  
---  
  
## 🔧 Options:  
  
```bash  
-l, --length         Password length (default: 12)  
  
--no-letters         Exclude letters (A-Z, a-z)  
  
--no-digits          Exclude digits (0-9)  
  
--no-symbols         Exclude symbols (e.g., !@#$%^&*)  
  
--exclude            Characters to exclude (e.g., 0OIl)  
  
--entropy            Display password entropy (in bits)  
  
--copy               Copy password to clipboard (requires pyperclip)  
```  
  
---  
  
## 🔍 Example Commands  
  
Generate a default 12-character password:  
  
```bash  
python passcraft.py  
```  
  
Generate a 20-character password excluding confusing characters:  
  
```bash  
python passcraft.py -l 20 --exclude 0OIl  
```  
  
Generate an 8-digit numeric-only password:  
  
```bash  
python passcraft.py -l 8 --no-letters --no-symbols  
```  
  
Generate a strong 16-character password, copy it, and view its entropy:  
  
```bash  
python passcraft.py -l 16 --copy --entropy  
```  
  
---  
  
## 🔐 Entropy Info  
  
Entropy measures how unpredictable your password is... higher = stronger.  
  
🧠  Formula:    
`entropy = log2(charset_size ^ length)`    
or    
`entropy = length × log2(charset_size)`  
  
> Example: A 16-character password using 62 characters (A-Z, a-z, 0-9) = ~95 bits of entropy    
> That’s **strong enough to resist brute-force attacks** for decades.  
  
---  
  
## 🧞 License  
  
MIT License. Use it, modify it, share it. Attribution appreciated.  
  
---  
  
## 🙋‍♂️ Contributing  
  
Bug reports and pull requests welcome.
Have a feature idea? Open an issue or PR..
  
---  
  
## 🌐 Author  
  
Made with clean code by **[ephemeral8997](https://github.com/ephemeral8997)**
