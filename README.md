# Mid
Returns the middle character of a given string.


<h2>How it works</h2>
<ul>
<li>A variable found is initialized as an empty string.</li>
<li>The function checks if the length of the word is even (len(word) % 2 == 0):</li>
    <ul>
      <li>If even, it immediately returns an empty string ("").</li>
    </ul>
<li>If odd, it calculates the middle character’s position with:</li>
  <ul>
    <li>index = len(word)/2 + 0.5 - 1</li>
  </ul>
<li>This formula ensures the result is centered for odd-length strings.</li>
<li>The function converts the result to an integer and returns the character at that position.</li>
</ul>

<h3>Example</h3>
result = mid("testing")
print(result)

<h3>Output</h3>
t

<h3>Example 2</h3>
result = mid("test")
print(result)

<h3>Output 2</h3>
""
