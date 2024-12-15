/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let current_num = init
    return {
        increment: function() {
            return ++current_num
        },
        reset: function() {
            current_num = init
            return current_num
        },
        decrement: function() {
            return --current_num
        }
        
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */