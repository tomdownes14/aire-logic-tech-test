# BUG TRACKER

## Can access other players' games

#### Steps

1. Clear browser data
2. Visit home page - http://35.176.178.218:8888/

#### Expected

Not able to see any games

#### Actual

Able to see all player games


## Cannot sell final cookie

#### Steps

1. Start new game - http://35.176.178.218:8888/
2. Click Cookie x1
3. Sell x1 Cookie

or   

1. Start new game - http://35.176.178.218:8888/
2. Click Cookie x10
3. Sell x10 Cookie
4. Sell x9 Cookie

#### Expected

All cookies to be sold. 

#### Actual

Final cookie cannot be sold.

## Cookies do not increase automatically with factories

#### Steps

1. Start new game - http://35.176.178.218:8888/
2. Click & Sell Cookies
3. Buy a factory
4. Wait

#### Expected

Cookies increase without clicking

#### Actual

Cookies only increase after clicking

## Can buy factory without cash

#### Steps

1. Start new game - http://35.176.178.218:8888/
2. Do not click for cookies
3. Buy a factory

#### Expected

Cannot purchase factory

#### Actual

Purchase factory and money value becomes negative
