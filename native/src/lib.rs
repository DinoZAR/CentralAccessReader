#[macro_use]
extern crate neon;
// extern crate objc

use neon::vm::{Call, JsResult};
use neon::js::JsString;
// use objc::{Class, send_msg};

fn hello(call: Call) -> JsResult<JsString> {
    let scope = call.scope;
    let args = call.arguments;
    let thing = call.arguments.get(0);
    Ok(JsString::new(scope, "hello node").unwrap())
}

// fn say(call: Call) -> JsResult<JsString>{
//     //let cls = Class::get("NSSpeechSynthesizer").unwrap()
//     let strcls = Class::get("NSString").unwrap()
//     let strobj: *mut Object = msg_send![strcls, new]
//     // msg_send![cls, startSpeakingString:text]
//     Ok(JsString::new(scope, "Neat!")).unwrap()
// }

register_module!(m, {
    m.export("hello", hello)
    // m.export("say", say)
});
