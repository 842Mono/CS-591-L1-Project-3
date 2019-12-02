const jiff = require('./jiff/lib/jiff-client.js');
const UI = require('./UI.js');
const mpc = require('./mpc.js')

jiff.make_jiff('http://localhost:3000', 'problem1', { crypto_provider: true, party_count: 2, onConnect: onConnect, party_id: 1});

async function onConnect(jiff_instance) {
  UI.clear();

  // ADD YOUR CODE HERE
  console.log('All connected');


  const CardsDrawn = []
  const PlayersCards = []
  const DealersCards = []

  let PlayerTotal = 0;
  let DealerTotal = 0;

  const getVal = (b1, b2) =>
  {
    const params = {upper_bound: b1, lower_bound: b2};
    const sampled_share_bits = jiff_instance.protocols.bits.rejection_sampling(null, null, null, null, params, null).share; // returns result as shares of bits
    return jiff_instance.protocols.bits.bit_composition(sampled_share_bits); // transforms bits to number
  }

  let PlayerRandomCard1Value = getVal(14, 1);
  let PlayerRandomCard1Suit = getVal(4, 1);



  jiff_instance.open(PlayerRandomCard1Value).then( a =>
  {
    // console.log('PlayerRandomCard1Value:');
    // console.log(a);
    jiff_instance.open(PlayerRandomCard1Suit).then( b =>
    {
      // console.log('PlayerRandomCard1Suit:');
      // console.log(b);

      CardsDrawn.push([a, b]);
      PlayersCards.push([a, b]);
      PlayerTotal += a;

      let DealerRandomCard1Value = getVal(14, 1);
      let DealerRandomCard1Suit = getVal(4, 1);
      jiff_instance.open(DealerRandomCard1Value).then( c =>
      {
        // console.log('DealerRandomCard1Value:');
        // console.log(c);
        jiff_instance.open(DealerRandomCard1Suit).then( d =>
        {
          // console.log('DealerRandomCard1Value:');
          // console.log(d);

          for(cd in CardsDrawn)
          {
            if(cd[0] == c && cd[1] == d)
              throw "Error unexpected duplicate. Try playing again."
          }
          CardsDrawn.push([c, d]);
          DealersCards.push([c, d]);
          DealerTotal += c;

          let PlayerRandomCard2Value = getVal(14, 1);
          let PlayerRandomCard2Suit = getVal(4, 1);
          jiff_instance.open(PlayerRandomCard2Value).then( e =>
          {
              // console.log('PlayerRandomCard1Value:');
              // console.log(c);
              jiff_instance.open(PlayerRandomCard2Suit).then( f =>
              {
                // console.log('PlayerRandomCard1Value:');
                // console.log(d);

                for(cd in CardsDrawn)
                {
                if(cd[0] == e && cd[1] == f)
                    throw "Error unexpected duplicate. Try playing again."
                }
                CardsDrawn.push([e, f]);
                PlayersCards.push([e, f]);
                PlayerTotal += e;



                let DealerRandomCard2Value = getVal(14, 1);
                let DealerRandomCard2Suit = getVal(4, 1);
                // need to check that card wasn't a duplicate.


                // console.log(CardsDrawn)
                console.log("Dealer's Cards: " + DealersCards);
                console.log("Player's Cards: " + PlayersCards);
                console.log("Player's Total: " + PlayerTotal);


                // return Promise({CardsDrawn:CardsDrawn, PlayersCards:PlayersCards, DealersCards:DealersCards, dc2v:DealerRandomCard2Value, dc2s:DealerRandomCard2Suit})

                //player's turn
                // UI.readboolean();

                jiff_instance.listen('cardDrawn', function (id, msg) {


                  // card = JSON.parse(msg);
                  // CardsDrawn.push(card);
                  // PlayersCards.push(card);
                  // PlayerTotal += card[0];

                  let DealerRandomCard1Value = getVal(14, 1);
                  let DealerRandomCard1Suit = getVal(4, 1);
                  jiff_instance.open(DealerRandomCard1Value).then( newVal =>
                  {
                    // console.log('DealerRandomCard1Value:');
                    // console.log(c);
                    jiff_instance.open(DealerRandomCard1Suit).then( newSuit =>
                    {
                      // console.log('DealerRandomCard1Value:');
                      // console.log(d);
            
                      for(cd in CardsDrawn)
                      {
                        if(cd[0] == newVal && cd[1] == newSuit)
                          throw "Error unexpected duplicate. Try playing again."
                      }
                      CardsDrawn.push([newVal, newSuit]);
                      PlayersCards.push([newVal, newSuit]);
                      PlayerTotal += newVal;

                      console.log("Dealer's Cards: " + DealersCards);
                      console.log("Player's Cards: " + PlayersCards);
                      console.log("Player's Total: " + PlayerTotal);

                      if(PlayerTotal > 21)
                        console.log("Player Lost.");
                        UI.stop();
                    });
                  });


                  // console.log('received message from party', id, ':', msg);
                  // console.log("Dealer's Cards: " + DealersCards);
                  // console.log("Player's Cards: " + PlayersCards);
                  // console.log("Player's Total: " + PlayerTotal);
                });

                jiff_instance.listen('donewithcards', function (id, msg)
                {
                  

                  jiff_instance.open(DealerRandomCard2Value).then( newVal =>
                  {
                    // console.log('DealerRandomCard1Value:');
                    // console.log(c);
                    jiff_instance.open(DealerRandomCard2Suit).then( newSuit =>
                    {
                      // console.log('DealerRandomCard1Value:');
                      // console.log(d);

                      for(cd in CardsDrawn)
                      {
                        if(cd[0] == newVal && cd[1] == newSuit)
                          throw "Error unexpected duplicate. Try playing again."
                      }
                      CardsDrawn.push([newVal, newSuit]);
                      DealersCards.push([newVal, newSuit]);
                      DealerTotal += newVal;

                      console.log("Dealer's Total: " + DealerTotal);

                      if(DealerTotal >= 17)
                      {
                        if(DealerTotal > 21)
                        {
                          console.log("Dealer Lost");
                        }
                        else
                        {
                          if(DealerTotal == PlayerTotal)
                            console.log("Draw");
                          if(DealerTotal > PlayerTotal)
                            console.log("Dealer Won.");
                          if(DealerTotal < PlayerTotal)
                            console.log("Player Won.");
                        }
                        UI.stop()
                      }
                      else
                      {
                        let f2 = () =>
                        {

                          let DealerRandomCard1Value = getVal(14, 1);
                          let DealerRandomCard1Suit = getVal(4, 1);
                          jiff_instance.open(DealerRandomCard1Value).then( newVal =>
                          {
                            // console.log('DealerRandomCard1Value:');
                            // console.log(c);
                            jiff_instance.open(DealerRandomCard1Suit).then( newSuit =>
                            {
                              // console.log('DealerRandomCard1Value:');
                              // console.log(d);
                    
                              for(cd in CardsDrawn)
                              {
                                if(cd[0] == newVal && cd[1] == newSuit)
                                  throw "Error unexpected duplicate. Try playing again."
                              }
                              CardsDrawn.push([newVal, newSuit]);
                              DealersCards.push([newVal, newSuit]);
                              DealerTotal += newVal;
                            
                              console.log("Dealer's Total: " + DealerTotal);

                              if(DealerTotal >= 17)
                              {
                                if(DealerTotal > 21)
                                {
                                  console.log("Dealer Lost");
                                }
                                else
                                {
                                  if(DealerTotal == PlayerTotal)
                                    console.log("Draw");
                                  if(DealerTotal > PlayerTotal)
                                    console.log("Dealer Won.");
                                  if(DealerTotal < PlayerTotal)
                                    console.log("Player Won.");
                                }
                                UI.stop()
                              }
                              else
                              {
                                f2();
                              }

                              
                            });
                          });
                          
                        }
                        f2();
                      }
                    });
                  });

                  // console.log('received message from party', id, ':', msg);
                });





              });
          });
        });
      });
    });
  });




  // listen to some communication/messages from player
  jiff_instance.listen('test-emit', function (id, msg) {
    // this callback will be executed for every 'test-emit' message received from the player
    console.log('received message from party', id, ':', msg);
  });
  
  // Sample under MPC in [1,14)
  const params = {upper_bound: 14, lower_bound: 1};
  const sampled_share_bits = jiff_instance.protocols.bits.rejection_sampling(null, null, null, null, params, null).share; // returns result as shares of bits
  const sampled_share_number = jiff_instance.protocols.bits.bit_composition(sampled_share_bits); // transforms bits to number
  const sampled_value = await jiff_instance.open(sampled_share_number); // returns a promise

  // add your code here
  // UI.display([sampled_value, 'X'], ['X', 'X']);

  // when everything is done
  // jiff_instance.disconnect(true, true);
  // UI.stop();
}
