# Santa's Little Helper

```
                 ######%##**####*######*##                                                          
               #%*+++*%*+++++++*%*+++++++*%*                                                        
              *%++*%#++++++++++*#+*++++++++%                                                        
             *%++*####*+++*#**++###%#++++++%+                                                       
             #*+*+:...:+#=:..:-*++++**+++++%=                                                       
             ##*#.-:. .*.. ..:..#++++#*+++*#                                                        
               =*.=-...*....+*..#+++++%***%                                                         
                *%-..:+%=......+*+++++%++                                                           
               ##++++++++*#**#*++++++*%                                                             
    %#      +#%*+++++++++++++++++++++#*                                                             
  #%@%%%##%#**+++++++++++++++++++++++%                                                              
  %@@@@@#++++++++++++++++++++++++++++#                                                              
  *%%@@%*++++++++++++++++++++++++++++#*                                                             
      ##*++++++++++++*#%%###*+++++++++#                                                             
         *#%%%%%%%%**  ##+++++++++++++#*                                                            
                        +##++++++++++++#                                                            
                          *#+++++++++++*%                                                           
                           #++++++++++++*#                                                          
                           #+++++++++++++*#                                                         
                          *#++++++++++++++*#                                                        
                          #*++++++++++++++++%+                                                      
                         +%++++++++++++++++++##                                                     
                         #*+++++++++++++++++++*#*                                                   
                         #++++++++++++++++++++++*%#                                                 
                        :#++++++++++++++++++++++++#%*                                               
                        :#++++++++++++++++++++++++++###                                             
                         %++++++++++++++++++++++++++++#%                                            
                         *#+++++#+++++++++++++++++++++++*%+                                         
                         ##*+++*#+++++++++*+*+++++++++++++*##                                       
                         %+*#+++#+++++++++##*+++++++++++++++*##                                     
                         #*++#*+%+++++++++**++**++++++++++++++*##                                   
                         **+++*##*+++++++++%*%*+++++++*%%%%%#*++*##                                 
                         =#++++++%+++++++++**++*%+++%#++++++++*%++##                                
                          #*+++++*#+++++++++#++++++#*+++++++++++*#++#*                              
                          *%++++++%*+++++++++%#*##*#++++++++++++++#*+##                             
                           #++++++###++++++++*###+#*+++++++++++++++#*+##                            
                           #++++++*##%*+++++++%**+**++++++++++++++++#++##                           
                          *#++++++#* =#++++++*###++#+++++++++++++++++*++#*                          
                          +#+++++##   #++++++#**#++#++++++++++++++++++++*#                          
                          *#+++++%    %*+++++%  #++*#++++++++++++++++++++#+                         
                          #*++++##    %*++++##  ##++**+++++++++**++++++++**                         
                          %++++*%     ##++++%+   #+++#*++++++++*#++++++++*#                         
                         +#++++#*     *#+++*#    *#+++#*++++++++%++++++++*#                         
                         ##+++*%      +#+++##     *#+++*#+++++++*#+++++++##                         
                         #*+++#*      *#+++%=      +#++++%+++++++#*++++++%+                         
                         %++++%       ##++*%        +#*+++*#++++++#*++++#**#%#=                     
                        *#+++##      #%*++*#+*   =*#%##+++++#*+++++#*++#*+++++***###%%#%%%##**      
                       *%*+++%     *#*#*++#********++++++++**%#+++++*##%#****+++++++++++++++***#%   
                    ###**+++##     *#*%+++%*###***#############++++++#%    *##%#%%%%%####%%#**++*#  
                   *#++++++%#        *#+++%     ##*########*+++++++*#%+                      *#++#  
                    ###*##%*      *#%%*++%#    ##+++++++++*######*                        *#%#+*%*  
                                 #*+++++%*     *%#######*#                     *#%%%%%%##***####    
                                 %#****##        #*#*                              ####%%%###       
                                  *#%##
```

Scripts for [Advent of Code](https://adventofcode.com).

## Installation

SLH is probably easiest to install with pipx.

```console
$ pipx install git+https://github.com/tjsmart/slh
```

## Config

SLH is configured via a configuration file which should be in
the current working directory with the name `./.slh-config.json`.

Example file contents:
```json
{
  "language": "c"
}
```

| field    | required | type   | description                                                   |
| -------- | -------- | ------ | ------------------------------------------------------------- |
| language | yes      | string | programming language, case-insentive, examples: "c", "python" |

## Next

This is the first command you will want to run. It will create src files,
download prompts, input and other stuff. Works with a new project, just
need to specify a minimal config.

```console
$ slh next --help
usage: slh next [-h]

Generate files for next day/part.

options:
  -h, --help  show this help message and exit
```

## Run

This is the second command you will want to run. It will run the
provided day/part puzzle. By default this will run the latest
created puzzle.

```console
$ slh run --help                                                               185ms
usage: slh run [-h] [--all] [--days DAYS] [--parts PARTS] [--test] [--count COUNT]

Execute specified solutions, by default the most recent solution is executed.

options:
  -h, --help     show this help message and exit
  --all
  --days DAYS
  --parts PARTS
  --test
  --count COUNT
```

## Submit

This is the final command you will want to run. It will submit the
provided day/part puzzle.

```console
$ slh submit --help                                                               185ms
usage: slh submit [-h]

Submit the specified solutions, by default the most recent solution is submitted.

options:
  -h, --help  show this help message and exit
```
