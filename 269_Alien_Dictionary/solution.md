# Solution

URL: https://leetcode.com/problems/alien-dictionary/solution/

---

This article assumes you already have some confidence with graph algorithms, such as breadth-first search and depth-first searching. If you're familiar with those, but not with topological sort (the topic tag for this problem), don't panic, as you should still be able to make sense of it. It is one of the many more advanced algorithms that keen programmers tend to "invent" themselves before realizing it's already a widely known and used algorithm. There are a couple of approaches to topological sort; Kahn's Algorithm and DFS.

A few things to keep in mind:

- The letters within a word don't tell us anything about the relative order. For example, the presence of the word kitten in the list does not tell us that the letter k is before the letter i.
- The input can contain words followed by their prefix, for example, abcd and then ab. These cases will never result in a valid alphabet (because in a valid alphabet, prefixes are always first). You'll need to make sure your solution detects these cases correctly.
- There can be more than one valid alphabet ordering. It is fine for your algorithm to return any one of them.
- Your output string must contain all unique letters that were within the input list, including those that could be in any position within the ordering. It should not contain any additional letters that were not in the input.

---

## Overview of Approaches

All approaches break the problem into three steps.

- Extracting dependency rules from the input. For example "A must be before C", "X must be before D", or "E must be before B".
- Putting the dependency rules into a graph with letters as nodes and dependencies as edges (an adjacency list is best).
- Topologically sorting the graph nodes.

We encourage you to go and have another go at implementing these steps yourself if you think you now know what to do. If this all sounded overwhelming and confusing though, don't panic, because we're going to work through it all in detail.

---

## Approach 1: Breadth-First Search

### Intuition

There are three parts to this problem.

1. Getting as much information about the alphabet order as we can out of the input word list.
2. Representing that information in a meaningful way.
3. Assembling a valid alphabet ordering.

### Part 1: Extracting Information

Let's start with a large example of a dictionary in an "alien language", and see how much we can conclude with some simple reasoning. This is likely to be your first step in tackling this question in a programming interview.

TODO image

Remember that in an ordinary English dictionary, all the words starting with a are at the start, followed by all the ones starting with b, then c, d, e, and at the very end, z. In the "alien dictionary", we also expect the first letters of each word to be in alphabetical order. So, let's look at them.

TODO image

Removing the duplicates, we get:

TODO image

Going by this, we know the relative order of four letters in the "alien dictionary". However, we don't know how these four letters fit in with the other seven letters, or even how those other seven letters fit in with each other. To get more information, we'll need to look further.

Going back to the English dictionary analogy, the word abacus will appear before algorithm. This is because when the first letter of two words is the same, we instead look at the second letter; b and l in this case. b is before l in the alphabet.

Let's take a closer look at the first two words of the "alien dictionary"; wxqkj and whgg. Seeing as the first letters are the same, w, we look at the second letters. The first word has x, and the second word has h. Therefore, we know that x is before h in the alien dictionary. We know have two fragments of the letter-order.

TODO image

We don't know yet how these two fragments could fit together into a single ordering. For example, we don't know whether w is before x, or x is before w, or even whether or not there's enough information available in the input for us to know.

Anyway, we've now gotten all the information we can out of the first two words. All letters after x in wxqkj, and after h in whqg, should be ignored because they did not impact the relative ordering of the two words (if you're confused, think back to abacus and algorithm. Because b > l, the gorithm and acus parts are unimportant for determining alphabetical ordering).

Hopefully, you're starting to see a pattern here. Where two words are adjacent, we need to look for the first difference between them. That difference tells us the relative order between two letters. Let's have a look at all the relations we can find by comparing adjacent words.

TODO image

You might notice that we haven't included some rules, such as w → j. This is fine though, as we can still derive it from the rules we have: w → c, c → k, k → j.

This completes the first part. There is no further information we can extract from the input. Therefore, our task is now to put together what we know.

### Part 2: Representing the Relations

We now have a set of relations stating how pairs of letters are ordered relative to each other.

TODO image

How could we put these together? You may be tempted to start trying to build "chains" out of them. Here are a few possible chains.

TODO image

Some combined chains: w→c→k→j, w→c→d, x→c→k→j, and q→m

The problem here though is that some letters are in more than one chain. Simply putting the chains into the output list one-after-the-other won't work. Some letters will be duplicated, which invalidates the ordering. Simply deleting the duplicates will not work either.

When we have a set of relations, often drawing a graph is the best way to visualize them. The nodes are the letters, and an edge between two letters, A and B represents that A is before B in the "alien alphabet".

TODO image

### Part 3: Assembling a Valid Ordering

As we can see from the graph, four of the letters have no arrows going into them. What this means is that there are no letters that have to be before any of these four (remember that the question states there could be multiple valid orderings, and if there are, then it's fine for us to return any of them).

TODO image

Therefore, a valid start to the ordering we return would be:

First group ordering: q w t x

We can now remove these letters and edges from the graph, because any other letters that required them first will now have this requirement satisfied.

Graph after first step with new sources highlighted

On this new graph, there are now three new letters that have no in-arrows. We can add these to our output list.

Two groups ordering: q w t x, m h c

Again, we can remove these from the graph.
