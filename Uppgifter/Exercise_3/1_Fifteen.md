In this exercise we will develop a model class for the [Fifteen Puzzle](https://en.wikipedia.org/wiki/15_puzzle):

<table style="background: black; border-spacing: 2px; padding: 3px; font-size: 25px; text-align: right;">
  <tbody>
    <tr>
      <td style="color: white; background: red; padding: 4px;">1</td>
      <td style="color: red; background: white; padding: 4px;">2</td>
      <td style="color: white; background: red; padding: 4px;">3</td>
      <td style="color: red; background: white; padding: 4px;">4</td>
    </tr>
    <tr>
      <td style="color: white; background: red; padding: 4px;">5</td>
      <td style="color: red; background: white; padding: 4px;">6</td>
      <td style="color: white; background: red; padding: 4px;">7</td>
      <td style="color: red; background: white; padding: 4px;">8</td>
    </tr>
    <tr>
      <td style="color: white; background: red; padding: 4px;">9</td>
      <td style="color: red; background: white; padding: 4px;">10</td>
      <td style="color: white; background: red; padding: 4px;">11</td>
      <td style="color: red; background: white; padding: 4px;">12</td>
    </tr>
    <tr>
      <td style="color: white; background: red; padding: 4px;">13</td>
      <td style="color: red; background: white; padding: 4px;">14</td>
      <td style="color: white; background: red; padding: 4px;">15</td>
      <td style="color: red; background: white; padding: 4px;"></td>
    </tr>
  </tbody>
</table>

The easiest way to model the state of the puzzle is via a list of four rows, where each row itself is a list with four integers. The integers in each row represent the numbers shown in the individual blocks in the puzzle. When the number is 0 then this would mean that the corresponding position is the hole. The skeleton of the `FifteenModel` class is given bellow, your task is to complete the methods:
