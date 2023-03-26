# Practical Python Project
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Project \n",
    "- Modular Aritmetic\n",
    "- Conditiobal Statement\n",
    "- Checking equality\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Modular Operator %\n",
    "\n",
    "5 % 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "6 % 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "7 % 8"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Conditionals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "caan only see rated PG movies\n"
     ]
    }
   ],
   "source": [
    "age = 17\n",
    "if age > 17 :\n",
    "    print(\"can see a rated R movies\")\n",
    "elif age <17 and age >12:\n",
    "    print(\"can see the rated PG- 13 movies\")   \n",
    "else:\n",
    "    print(\"can only see rated PG movies\")     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "can only see rated PG movies\n"
     ]
    }
   ],
   "source": [
    "age = 12\n",
    "if age > 17 :\n",
    "    print(\"can see a rated R movies\")\n",
    "elif age <17 and age >12:\n",
    "    print(\"can see the rated PG- 13 movies\")   \n",
    "else:\n",
    "    print(\"can only see rated PG movies\")     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "can see the rated PG- 13 movies\n"
     ]
    }
   ],
   "source": [
    "age = 15\n",
    "if age > 17 :\n",
    "    print(\"can see a rated R movies\")\n",
    "elif age <17 and age >12:\n",
    "    print(\"can see the rated PG- 13 movies\")   \n",
    "else:\n",
    "    print(\"can only see rated PG movies\")     "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Equality "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the varible does not have the values of 3\n"
     ]
    }
   ],
   "source": [
    "a =6\n",
    "if a == 3:\n",
    "    print(\"the variable of values 3\")\n",
    "elif a != 3:\n",
    "    print(\"the varible does not have the values of 3\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the variable of values 3\n"
     ]
    }
   ],
   "source": [
    "a =3\n",
    "if a == 3:\n",
    "    print(\"the variable of values 3\")\n",
    "elif a != 3:\n",
    "    print(\"the varible does not have the values of 3\")    "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# List less than ten"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [1,1,2,3,8,13, 21, 34, 55 ,89]\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list = [a<5]\n",
    "my_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = []\n",
    "X.append(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_list1 = [1,3,\"Tayyaba\" , [3,4,5]]\n",
    "for element in my_list1:\n",
    "    print(element)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "grade = input(\"Enter your grade : \")\n",
    "if grade >=90:\n",
    "    print(\"A\")\n",
    "elif grade>= 80:\n",
    "    print(\"B\")   \n",
    "elif grade >=70:\n",
    "    print(\"C\")\n",
    "elif grade >=65:\n",
    "    print(\"D\") \n",
    "else:\n",
    "    print(\"F\")            "
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# List of Overlap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [ 1,1,2,3,,8,13,21,34,55,89]\n",
    "b = [1,2,3,4,5,6,7,8,9,10,11,12,13]\n",
    "# write the function that return the list conyaining only common element (without dublication)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# List Propertises"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [ 5,10, 15 ,20]\n",
    "10 in a\n",
    "3 in a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_students = ['Tayyaba ' , 'Fatima ' , 'Amina']\n",
    "name = input('Type name pf check: ')\n",
    "if name in list_of_students:\n",
    "    print(\"This student is enrolled\")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "years_of_brith = [1990 , 1991, 1990, 1990, 1992 , 1991]\n",
    "ages = []\n",
    "for year in years_of_brith:\n",
    "    ages.append(2014 - year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "years_of_brith = [1990 , 1991, 1990, 1990, 1992 , 1991]\n",
    "ages = [2014 - year  for year in years_of_brith]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Random Passward Renerator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# ASCII Code\n",
    "import random\n",
    "uppercaseLetter=chr(random.randint(65,90))\n",
    "# later doing"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
