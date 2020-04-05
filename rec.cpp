void printReverse(const char *str) {
  if (!*str)
    return;
  printReverse(str + 1);
  putchar(*str);
}

void main()
{
    char ch[100];
    ch = "12345"
    printReverse(ch);
}
