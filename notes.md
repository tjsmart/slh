# TODO:
- [x] cleanup
- [x] works for python
- [x] supports plugins
- [x] works for c

- [x] start previous aoc year with plugin
    - [ ] work out kinks
        - [ ] slh run doesn't run latest/current
        - [ ] cmakelists.txt issues (append new doesn't work and target collisions)
        - [ ] debug improvements
        - [ ] testing
        - [ ] LSP!!
    - [ ] develop slh lib
        - [x] read file
        - [ ] link list
        - [ ] hash map
        - [ ] points
        - [ ] matrix

- [ ] run without submit (for debugging without getting errors)

# Eventually:
- [ ] tests work

hashing: http://www.cse.yorku.ca/~oz/hash.html

# Random Thoughts:

- run --all filter unsolved problems (just print they are unsolved)
    - this may already work

- next fetches part2 even if part1 is not solved
    - opposed to fetching the next day? I'm not sure what I meant here

- grid helper class
    - transpose, iter_cols, iter_rows, rotations

- run with pypy
    - pypy only supports 3.10, 3.9 -- would need to strip out/conver type syntax to run in pypy

- better tracking of submitted solutions
    - only write solution*txt when correct answer is submitted
    - save guesses as too low/too high, use to avoid submitting incorrect answers

- better parsing the result from submit
    - parse wait time and wait until we can submit again (user can ctrl-c if they don't want to wait)

- add solution times to README.md

- profiling support
