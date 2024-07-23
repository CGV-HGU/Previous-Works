#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x30ff7695, "module_layout" },
	{ 0xc1f851b8, "param_ops_charp" },
	{ 0x83253110, "param_ops_bool" },
	{ 0xbc0b22e9, "param_array_ops" },
	{ 0xf9418c06, "param_ops_int" },
	{ 0xfd14437d, "video_ioctl2" },
	{ 0xf508bab2, "v4l2_event_unsubscribe" },
	{ 0x736f5b91, "nonseekable_open" },
	{ 0xdaf5fc38, "noop_llseek" },
	{ 0xef697d16, "misc_deregister" },
	{ 0x5ab14eb2, "misc_register" },
	{ 0x6d16c104, "mutex_lock_killable" },
	{ 0x3213f038, "mutex_unlock" },
	{ 0xac7ab837, "_dev_err" },
	{ 0x7665a95b, "idr_remove" },
	{ 0xf2133d3c, "device_create_file" },
	{ 0xdb714c58, "__video_register_device" },
	{ 0xd9a5ea54, "__init_waitqueue_head" },
	{ 0x5bc753bd, "v4l2_ctrl_handler_setup" },
	{ 0xe3d79eeb, "v4l2_ctrl_new_custom" },
	{ 0xd59b4b2, "v4l2_ctrl_handler_init_class" },
	{ 0xc6f46339, "init_timer_key" },
	{ 0xb58f9fe7, "video_device_release" },
	{ 0xee33c8c8, "video_device_alloc" },
	{ 0x2f319651, "v4l2_device_register" },
	{ 0xb8f11603, "idr_alloc" },
	{ 0x1d81f6f9, "v4l2_ctrl_subscribe_event" },
	{ 0xc6cc34f, "v4l2_event_subscribe" },
	{ 0xa4c7085, "v4l2_event_pending" },
	{ 0x65487097, "__x86_indirect_thunk_rax" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0x92540fbf, "finish_wait" },
	{ 0x8c26d495, "prepare_to_wait_event" },
	{ 0x1000e51, "schedule" },
	{ 0xfe487975, "init_wait_entry" },
	{ 0x69acdf38, "memcpy" },
	{ 0x800473f, "__cond_resched" },
	{ 0xf036341f, "_dev_warn" },
	{ 0x54b1fac6, "__ubsan_handle_load_invalid_value" },
	{ 0x1d24c881, "___ratelimit" },
	{ 0x33a21a09, "pv_ops" },
	{ 0xba8fbd64, "_raw_spin_lock" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x7f02188f, "__msecs_to_jiffies" },
	{ 0xe46021ca, "_raw_spin_unlock_bh" },
	{ 0xc3690fc, "_raw_spin_lock_bh" },
	{ 0xc38c83b8, "mod_timer" },
	{ 0x15ba50a6, "jiffies" },
	{ 0x97934ecf, "del_timer_sync" },
	{ 0xac37c85, "v4l2_fh_exit" },
	{ 0x9a92d940, "v4l2_fh_del" },
	{ 0x28b12cc9, "v4l2_format_info" },
	{ 0x6e9acc41, "v4l2_fill_pixfmt_mp" },
	{ 0xcc501597, "v4l2_fill_pixfmt" },
	{ 0x8e17b3ae, "idr_destroy" },
	{ 0x1d40b6f3, "idr_for_each" },
	{ 0xccb0e318, "vm_insert_page" },
	{ 0xc82c6e84, "vmalloc_to_page" },
	{ 0xd6ee688f, "vmalloc" },
	{ 0x12825e7b, "v4l2_fh_add" },
	{ 0xfa25b7c, "v4l2_fh_init" },
	{ 0x4f00afd3, "kmem_cache_alloc_trace" },
	{ 0xac1c4313, "kmalloc_caches" },
	{ 0x5e515be6, "ktime_get_ts64" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0xdd64e639, "strscpy" },
	{ 0xa916b694, "strnlen" },
	{ 0x87a21cb3, "__ubsan_handle_out_of_bounds" },
	{ 0x6ed15256, "video_devdata" },
	{ 0x40a9b349, "vzalloc" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x5c3c7387, "kstrtoull" },
	{ 0x656e4a6e, "snprintf" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0x20978fb9, "idr_find" },
	{ 0xd85527b3, "v4l2_ctrl_handler_free" },
	{ 0xd4254459, "v4l2_device_unregister" },
	{ 0x26fa9659, "video_unregister_device" },
	{ 0x37a0cba, "kfree" },
	{ 0x31a4886e, "device_remove_file" },
	{ 0x999e8297, "vfree" },
	{ 0x92997ed8, "_printk" },
	{ 0xa22a96f7, "current_task" },
	{ 0xd0da656b, "__stack_chk_fail" },
	{ 0x57cbff6e, "v4l2_event_queue" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "videodev");


MODULE_INFO(srcversion, "F787587E259AE5311BBD3D5");
