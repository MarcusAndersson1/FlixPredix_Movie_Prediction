<template>
    <Popover class="relative bg-white">
      <div class="mx-auto max-w-7xl px-4 sm:px-6">
        <div class="flex items-center justify-between border-b-2 border-gray-100 py-6 md:justify-start md:space-x-10">
          <div class="flex justify-start lg:w-0 lg:flex-1">
            <a href="/">
              <span class="sr-only">Movie Prediction</span>
              <img class="h-8 w-auto sm:h-10" src="../assets/felix.png" alt="" />
            </a>
          </div>
  
          <PopoverGroup as="nav" class="hidden items-center space-x-10 md:flex">
  
            <a href="/" class="text-base font-medium text-gray-500 hover:text-gray-900">Home</a>
            <a href="/#/analytics" class="text-base font-medium text-gray-500 hover:text-gray-900">Analytics</a>

          </PopoverGroup>
        </div>
      </div>
  

    </Popover>
  </template>
  
  <script setup>
  import { Popover, PopoverButton, PopoverGroup, PopoverPanel } from '@headlessui/vue'
  </script>