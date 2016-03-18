#include <iostream>

int endian(){
  int * one = new int(1);
  char * p0 = (char*)one;
  std::cout << (*one) << std::endl;
  std::cout << (*p0)-'a' << std::endl;
  p0++;
  std::cout << (*p0)-'a' << std::endl;
  p0++;
  std::cout << (*p0)-'a' << std::endl;
  p0++;
  std::cout << (*p0)-'a' << std::endl;
  return 0;
}

int main(){
  std::cout << "hello world" << std::endl;
  endian();
}
