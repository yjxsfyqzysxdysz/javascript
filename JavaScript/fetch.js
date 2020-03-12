/**
 * 基于 promise ？？？
 * Fetch 提供了对 Request 和 Response （以及其他与网络请求有关的）对象的通用定义。使之今后可以被使用到更多地应用场景中：无论是 service worker、Cache API、又或者是其他处理请求和响应的方式，甚至是任何一种需要你自己在程序中生成响应的方式。
 * 它同时还为有关联性的概念，例如CORS和HTTP原生头信息，提供一种新的定义，取代它们原来那种分离的定义。
 * 发送请求或者获取资源，需要使用 WindowOrWorkerGlobalScope.fetch() 方法。它在很多接口中都被实现了，更具体地说，是在 Window 和 WorkerGlobalScope 接口上。因此在几乎所有环境中都可以用这个方法获取到资源。
 * fetch() 必须接受一个参数——资源的路径。无论请求成功与否，它都返回一个 Promise 对象，resolve 对应请求的 Response。你也可以传一个可选的第二个参数 init（参见 Request）。
 * 一旦 Response 被返回，就可以使用一些方法来定义内容的形式，以及应当如何处理内容（参见 Body）。
 * 你也可以通过 Request() 和 Response() 的构造函数直接创建请求和响应，但是我们不建议这么做。他们应该被用于创建其他 API 的结果（比如，service workers 中的 FetchEvent.respondWith）。
 */

// https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API
