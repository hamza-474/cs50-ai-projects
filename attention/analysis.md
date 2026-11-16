# Analysis

## Layer 4, Head 10

In this head, a word that introduces a noun phrase -- a preposition, and likewise a determiner -- attends strongly to the head noun of that noun phrase, rather than to the word immediately after it. In the attention diagrams (for example, `Attention_Layer4_Head10.png`), the row for a preposition such as `on` or `in` is lightest, meaning highest attention, in the column of the noun that follows it, while the intervening determiner or adjective is much darker.

For the masked sentences below, the preposition attends to the masked noun, not to the determiner in between: in "The dog sat on the [MASK].", `on` attends 0.739 to `[MASK]` and only 0.224 to `the`; in "She put the key in the [MASK].", `in` attends 0.797 to `[MASK]` and only 0.174 to `the`; in "The book on the [MASK] is red.", `on` attends 0.684 to `[MASK]` and only 0.266 to `the`. Determiners behave the same way: in "The [MASK] sat on the mat.", `the` attends 0.914 to `[MASK]`, and in "She put the [MASK] in the box.", `the` attends 0.887 to `[MASK]`.

The same pattern holds without a mask, and is even stronger there: `on` attends 0.757 to `mat`, `in` attends 0.935 to `box`, `on` attends 0.874 to `table`, `in` attends 0.965 to `palm`, and `of` attends 0.807 to `hand`, a mean of 0.872 across those five preposition-to-noun pairs, and determiners attend to their nouns with a mean of 0.84 across eight examples. It also skips adjectives: in "Holmes sat in the red armchair.", `in` attends most to `armchair` (0.582), ahead of `the` (0.171) and `red` (0.152). This is different from the Layer 3, Head 10 pattern in the specification, because the attended noun is usually two or three tokens after the preposition, not the next token, and the preposition gives little attention to that next token.

Example Sentences:
- "The dog sat on the [MASK]."
- "She put the key in the [MASK]."
- "The book on the [MASK] is red."

## Layer 9, Head 11

In this head, a reflexive pronoun attends to its antecedent -- the subject it refers back to -- even though that subject is several tokens earlier in the sentence. In the attention diagrams (for example, `Attention_Layer9_Head11.png`), the row for `himself`, `herself`, or `itself` is lightest in the column of the subject, and much darker elsewhere, including at the pronoun itself and at `[CLS]`.

For the masked sentences below, the reflexive pronoun still picks out its antecedent: in "Holmes [MASK] to himself.", `himself` attends 0.846 to `Holmes`; in "The dog [MASK] itself.", `itself` attends 0.722 to `dog`; in "John [MASK] himself.", `himself` attends 0.502 to `John`; and in "Mary [MASK] herself.", `herself` attends 0.506 to `Mary`. Without a mask, the same direct-object reflexives are stronger: `himself` attends 0.939 to `Holmes`, 0.852 to `John`, `herself` attends 0.812 to `Mary`, and `itself` attends 0.883 to `dog`, a mean of 0.872. Masking the verb draws some of the pronoun's attention to `[MASK]` itself, which explains the lower masked weights. This is different from the Layer 4, Head 11 pattern in the specification: the attending token is a pronoun, the attended token is an earlier noun or pronoun, not a verb, and the relationship is coreference, not modification of a verb by an adverb.

The pattern is strongest for singular direct-object reflexives. It is weaker in other uses: in "They taught themselves a lesson.", `themselves` attends 0.483 to `They`, and in "She looked at herself in the mirror.", `herself` attends only 0.278 to `She`, so this head identifies a typical reflexive-antecedent link rather than a rule that holds for every reflexive.

Example Sentences:
- "Holmes [MASK] to himself."
- "John [MASK] himself."
- "Mary [MASK] herself."
- "The dog [MASK] itself."
