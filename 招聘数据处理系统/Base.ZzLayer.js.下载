(function() {
	/*
	 *Author Liyao
	 *Date 2009-3-11
	 *Function ZzLayer class
	 */

	//check the class name , it will be replaced when existed
	if ( window.ZzLayer ) {
		alert( 'variable ZzLayer has been used,it will be replaced with _ZzLayer!' );
		window._ZzLayer = window.ZzLayer;
	}

	//constructor
	window.ZzLayer = function( param ) {

		param = param instanceof Object ? param : {};

		//$extends Base class
		//this.$extends( Base );
		Base.apply( this , [param] );

		//div控件
		this.div = document.createElement( 'div' );
		this.setContent( param.content );
		this.div.style.border = '0px';
		this.div.style.backgroundColor = '#ffffff';
		if(param.nobkcolor)
		{
			this.div.style.backgroundColor = '';		
		}
		if ( param.divProps ) {
			for (  var prop in param.divProps ) {
				if ( 'style' == prop ) {
					for ( var subProp in param.divProps[prop] ) {
						this.div[prop][subProp] = param.divProps[prop][subProp];
					}
				}
				else {
					this.div[prop] = param.divProps[prop];
				}
			}
		}
		this.div.style.position = 'absolute';//必要属性
		this.div.style.visibility = 'hidden';//必要属性
		this.div.style.display = 'block';//必要属性
		this.div.style.zIndex =  Math.max( this.div.style.zIndex , 50 );//必要属性
		this.backToLeftTop();
		var appendNode = this._( param.appendNode ) || document.body;
		appendNode.appendChild( this.div );
		
		//iframe控件
		if ( param.createIfr != undefined ? param.createIfr : true ) {
			this.ifr = document.createElement( 'iframe' );
			this.ifr.style.border = '0px';
			this.ifr.style.backgroundColor = '#ffffff';
			if ( param.ifrProps ) {
				for (  var prop in param.ifrProps ) {
					if ( 'style' == prop ) {
						for ( var subProp in param.ifrProps[prop] ) {
							this.ifr[prop][subProp] = param.ifrProps[prop][subProp];
						}
					}
					else {
						this.ifr[prop] = param.ifrProps[prop];
					}
				}
			}
			this.ifr.style.position = 'absolute';//必要属性
			this.ifr.style.visibility = 'hidden';//必要属性
			this.ifr.style.display = 'block';//必要属性
			this.ifr.style.zIndex = this.div.style.zIndex - 1;//必要属性
			this.backToLeftTop();
			appendNode.appendChild( this.ifr );

		}
		
		//拖曳控件
		this.setDragNode( param.dragNode );

		//关闭控件
		this.setCloseNode( param.closeNode );

		//接口方法
		this.beforeOpen = param.beforeOpen && typeof param.beforeOpen == 'function' ? param.beforeOpen : function(){};
		this.afterOpen = param.afterOpen && typeof param.afterOpen == 'function' ? param.afterOpen : function(){};
		this.beforeClose = param.beforeClose && typeof param.beforeClose == 'function' ? param.beforeClose : function(){};
		this.afterClose = param.afterClose && typeof param.afterClose == 'function' ? param.afterClose : function(){};

		//快捷关闭
		this.isQuickClose = param.isQuickClose != undefined ? param.isQuickClose : true;
		if ( !this.quickCloseProps.isBindDocEvt && this.isQuickClose ) {
			this.attEvt( document , 'keydown' , this.getQuickCloseFunc( this ) );
			this.quickCloseProps.isBindDocEvt = true;
		}
		this.quickColseIndex = -1;

		if ( param.MOutCloseNode ) {
			this.setMOutCloseNode( param.MOutCloseNode );
		}

	}.$extends( Base );
	
	//share property && method
	var pt = ZzLayer.prototype;

	pt.setMOutCloseNode = function( MOutCloseNode ) {
		this.MOutCloseNode = this._( MOutCloseNode );
		this.attEvt( this.MOutCloseNode ,	'mouseout' ,	this.getOnFunc( 'mouseout' ) );
		this.attEvt( this.MOutCloseNode ,	'mouseover' ,	this.getOnFunc( 'mouseover' ) );
		this.attEvt( this.div ,				'mouseover' ,	this.getOnFunc( 'mouseover' ) );
		this.attEvt( this.div ,				'mouseout' ,	this.getOnFunc( 'mouseout' ) );
	}

	pt.getOnFunc = function( type ) {
		var thisObj = this;
		function isClose() {
			if ( thisObj.canClose ) {
				thisObj.close();
			}
		}
		switch ( type ) {
			case 'click': return function( event ) {thisObj.open( event );};
			case 'mouseover': return function() {thisObj.canClose = false;};
			case 'mouseout': return function() {thisObj.canClose = true;setTimeout( isClose , 50 );};
		}
		return function(){};
	}
	
	pt.quickCloseProps = {
		isBindDocEvt : false ,
		toCloseObjs : []
	}

	pt.getQuickCloseFunc = function( zl ) {
		return function( event ) {
			zl.quickClose.apply( zl , [event] );
		}
	}

	pt.quickClose = function( event ) {//按ESC键关闭层
		event = event || window.event;
		if ( 27 == event.keyCode ) {
			var obj = this.quickCloseProps.toCloseObjs[this.quickCloseProps.toCloseObjs.length - 1];
			if ( obj ) {
				obj.close( {} ,event );
			}
		}
	}

	pt.pushToQuickCloseObjs = function() {
		this.delFromQuickCloseObjs();
		this.quickCloseProps.toCloseObjs.push( this );
		this.quickColseIndex = this.quickCloseProps.toCloseObjs.length - 1;
	}

	pt.delFromQuickCloseObjs = function() {
		if ( this.quickColseIndex >= 0 ) {
			for ( var i = this.quickColseIndex + 1 ; i < this.quickCloseProps.toCloseObjs.length ; i++ ) {
				this.quickCloseProps.toCloseObjs[i].quickColseIndex--;
			}
			this.quickCloseProps.toCloseObjs.splice( this.quickColseIndex , 1 );
			this.quickColseIndex = -1;
		}
	}

	pt.setDragNode = function( dragNode ) {
		if ( dragNode != undefined ) {
			dragNode = this._( dragNode );
			if ( dragNode && dragNode.nodeName ) {
				this.objX = this.ObjY = 0;
				this.attEvt( dragNode , 'mousedown' , this.getDragNodeMouseDownFunc( this ) );
				this.attEvt( document , 'mousemove' , this.getDocumentMouseMoveFunc( this ) );
				this.attEvt( document , 'mouseup' , this.getDocumentMouseUpFunc( this ) );
				dragNode.style.cursor = 'move';
				this.div.onselectstart = function() { return false; };
				if ( this.ifr ) {
					this.ifr.onselectstart = this.div.onselectstart;
				}
			}
		}
	}
	pt.setCloseNode = function( closeNode ) {
		if ( closeNode != undefined ) {
			closeNode = this._( closeNode );
			if ( closeNode && closeNode.nodeName ) {			
				this.attEvt( closeNode , 'click' , this.getCloseNodeClickFunc( this ) );
				closeNode.style.title = '关闭 (Esc)';
				closeNode.style.cursor = 'pointer';
			}
		}
	}


	pt.setContent = function ( content ) {
		if ( content != undefined && ( content.nodeName || typeof content == 'string' ) && this.removeContent() ) {
			if ( content.nodeName ) {
				this.div.appendChild( content );
			}
			else {
				this.div.innerHTML = content + '';
			}
			return true;
		}
		return false;
	}

	pt.getContent = function ( type ) {
		return 1 == type ? this.div.childNodes : this.div.innerHTML;
	}

	pt.removeContent = function() {
		try {
			for ( var i = 0 ; i < this.div.childNodes.length ; i++ ) {
				this.div.removeChild( this.div.childNodes[i] );
			}
			this.div.innerHTML = '';
			return true;
		}
		catch ( e ) {
		}
		return false;
	}

	pt.backToLeftTop = function() {
		this.div.style.left = this.div.style.top = '0px';
		if ( this.ifr ) {
			this.ifr.style.left = this.ifr.style.top = '0px';
		}
	}

	pt.resizeIfr = function() {
		if ( this.ifr ) {
			this.ifr.style.width = this.div.offsetWidth + 'px';
			this.ifr.style.height = this.div.offsetHeight + 'px';
		}
	}

	pt.syncPosIfr = function() {
		if ( this.ifr ) {
			this.ifr.style.left = this.div.style.left;
			this.ifr.style.top = this.div.style.top;
		}
	}

	pt.open = function() {

		var arg0 = arguments[0] instanceof Array ? arguments[0] : [arguments[0]];
		var arg1 = arguments[1] instanceof Array ? arguments[1] : [arguments[1]];

		this.beforeOpen.apply( this , arg0 );

		this.resizeIfr();
		this.syncPosIfr();
		this.div.style.visibility = 'visible';
		if ( this.ifr ) {
			this.ifr.style.visibility = 'visible';
		}

		if ( this.isQuickClose ) {
			this.pushToQuickCloseObjs();
		}

		this.afterOpen.apply( this , arg1 );
	}

	pt.close = function() {

		var arg0 = arguments[0] instanceof Array ? arguments[0] : [arguments[0]];
		var arg1 = arguments[1] instanceof Array ? arguments[1] : [arguments[1]];
		
		this.beforeClose.apply( this , arg0 );

		this.div.style.visibility = 'hidden';
		if ( this.ifr ) {
			this.ifr.style.visibility = 'hidden';
		}
		this.backToLeftTop();
		this.delFromQuickCloseObjs();

		this.afterClose.apply( this , arg1 );
	}
	
	pt.dragNodeMouseDown = function( event ) {
		event = event || window.event;
		this.objX = event.clientX - this.div.style.left.replace( /p|x/g , '' );
		this.objY = event.clientY - this.div.style.top.replace( /p|x/g , '' );
	}

	pt.documentMouseMove = function ( event ){
		if( this.objX != 0 && this.objY != 0 ) {
			event = event || window.event;
			if ( 1 == event.button ||  0 == event.button ) {

				this.div.style.left = Math.min( Math.max( document.body.scrollWidth , document.documentElement.scrollWidth ) - this.div.offsetWidth , Math.max( 0 , event.clientX - this.objX ) )+ 'px';

				this.div.style.top = Math.min( Math.max( 0 , event.clientY - this.objY ) , Math.max( document.body.scrollHeight , document.documentElement.scrollHeight ) - this.div.offsetHeight )+ 'px';

				this.syncPosIfr();
			}
		}
	}

	pt.documentMouseUp = function () {
		this.objX = this.objY = 0;
	}

	pt.getDragNodeMouseDownFunc = function ( zl ) {
		return function() {
			zl.dragNodeMouseDown.apply( zl , [arguments[0]] );
		}
	}

	pt.getDocumentMouseMoveFunc = function ( zl ) {
		return function() {
			zl.documentMouseMove.apply( zl , [arguments[0]] );
		}
	}

	pt.getDocumentMouseUpFunc = function ( zl ) {
		return function() {
			zl.documentMouseUp.apply( zl );
		}
	}

	pt.getCloseNodeClickFunc = function ( zl ) {
		return function() {
			zl.close.apply( zl );
		}
	}

})();